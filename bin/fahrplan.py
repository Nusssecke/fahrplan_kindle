import json
import logging
import ssl
import urllib.request
from datetime import datetime, timedelta


class Connection:
    """ A Connection object represents a journey/trip from start to endpoint. May include multiple trains.
    A connection is created out of a trip dictionary from the trips list(Response from the trip service).
    The leglist contains leg dictionaries(always one as per search parameters)(represents one train)
    A leg contains another dictionary which has origin, destination and product dictionaries"""

    url_journey_detail = 'https://www.rmv.de/hapi/journeyDetail'
    journey_detail_id: str

    departure: datetime  # Departure from the starting station
    arrival: datetime  # Arrival at the destination
    duration: datetime  # The duration of the whole journey
    train_type: str  # The train lines as comma separated list e.g. RB49, S6
    delay: int  # The delay in minutes; e.g. 12:12 + 5min
    train_changes: int  # How often you have to change trains

    def __init__(self, trip_dict):
        # Extract relevant information from the json response
        destination = trip_dict['LegList']['Leg'][0]['Destination']
        arrival_date_str = destination['date']  # Date without delay
        arrival_time_str = destination['time']  # Time without delay
        self.arrival = datetime.strptime(f'{arrival_time_str};{arrival_date_str}', '%H:%M:%S;%Y-%m-%d')

        origin = trip_dict['LegList']['Leg'][0]['Origin']
        departure_date_str = origin['date']
        departure_time_str = origin['time']
        self.departure = datetime.strptime(f'{departure_time_str};{departure_date_str}', '%H:%M:%S;%Y-%m-%d')

        if 'rtDate' in origin:  # Check if there is delay information
            delay_date_str = origin['rtDate']
            delay_time_str = origin['rtTime']
            delay_datetime = datetime.strptime(f'{delay_time_str};{delay_date_str}', '%H:%M:%S;%Y-%m-%d')
            self.delay = self.delay_to_minutes(delay_datetime)
        else:
            self.delay = 0

        self.duration = self.arrival - self.departure

        journey = trip_dict['LegList']['Leg'][0]['Product'][0]
        self.train_type = journey['line']

        self.train_changes = len(trip_dict['LegList']['Leg'])

        # journey_detail_ref = trip_dict['LegList']['Leg'][0]['JourneyDetailRef']
        # self.journey_detail_id = journey_detail_ref['ref']

    def in_the_past(self):
        """ Checks if a connection is in the past, considers delay

        :return: boolean: Is connection in the past"""
        # Parse string values of departure (with delay) and departure date to datetime objects and combine
        delay_datetime = self.departure + timedelta(minutes=self.delay)

        # Check if there is -1 day or more difference between the dates (date value subtraction)
        return (delay_datetime - datetime.now()).days < 0

    def delay_to_minutes(self, delay_datetime):
        """ Convert the delay from datetime to delay in minutes

        :return: Time delay in minutes"""
        time_delta = delay_datetime - self.departure

        return int(time_delta.seconds / 60)  # Convert to minutes

    def __eq__(self, other):
        return self.departure == other.departure and self.arrival == other.arrival and \
               self.train_type == other.train_type

    def __repr__(self):
        return f'Connection: Abfahrt: {self.departure} Ankunft: {self.arrival}' \
               f' Zug: {self.train_type} Verspätung: {self.delay}'


class Timetable:
    access_id: str  # Api key for making requests to the HAFAS Rest service
    connections: list[Connection] = []  # A list of all connections which fit(which have not passed, no train changes, etc.)

    url_trip = 'https://www.rmv.de/hapi/trip'
    trip_parameters = {
        'format': 'json',
        'originId': 'A=1@O=Bad+Nauheim+Bahnhof@X=8748320@Y=50367792@U=80@L=003011135@B=1@V=6.9,@p=1565110738@',
        'numF': '3',  # Number of trips found 6 is max
        'products': '12',  # Only allow trains(No buses)
        'maxChange': '1',  # Maximum number of train changes
    }

    def __init__(self, access_id, destination_station):
        self.access_id = access_id
        self.trip_parameters['accessId'] = access_id

        if destination_station == 'Frankfurt West':
            self.trip_parameters[
                'destId'] = 'A=1@O=Frankfurt+(Main)+Westbahnhof@X=8639452@Y=50119447@U=80@L=003001204@B=1@V=6.9,@p=1565110738@'
        elif destination_station == 'Gießen':
            self.trip_parameters[
                'destId'] = 'A=1@O=Gießen Bahnhof@X=8663803@Y=50579883@U=80@L=003011016@B=1@V=6.9,@p=1634845050@'

    def __str__(self):
        string = 'Timetable:\n'
        for connection in self.connections:
            string = string + '\t' + str(connection) + '\n'
        return string[:-1]

    def refresh(self):
        """The trip value in the main dict is a list
            The trip list contains dicts which represent a connection each"""

        logging.info('Loading connections')

        # Get new connections
        # Add the parameters to the url and open it
        ssl_context = ssl._create_unverified_context()
        response = urllib.request.urlopen(f'{self.url_trip}?{urllib.parse.urlencode(self.trip_parameters)}',
                                          context=ssl_context)

        json_data = json.loads(response.read())
        self.update_connections(json_data)

        # Sort connections by departure time
        self.connections.sort(key=lambda x: x.departure)

    def update_connections(self, json_data):
        self.connections = []  # Remove old connections
        # There is one trip dictionary for each connection
        for trip in json_data['Trip']:
            # Create connection from the trip of the response
            connection = Connection(trip)

            logging.info(f'Connection found: {connection} Already in connections: {connection in self.connections}')
            logging.info('\tConnection Added')
            self.connections.append(connection)
