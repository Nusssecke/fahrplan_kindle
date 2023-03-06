from datetime import datetime
import os
import sys
from os.path import join

# Check for system type for easier programming
from fahrplan import Timetable

# svg_path = 'C:\\Users\\finn-\\Programmieren\\KindleExtension\\fahrplan_kindle\\images'
svg_path = '/mnt/base-us/extensions/fahrplan_kindle/images/'


def create_svg(svg_data, svg_template, svg_output):
    with open(svg_template, 'r') as fin:
        template = fin.read()

        for k, v in svg_data.items():
            template = template.replace(k, v)

        with open(svg_output, 'w') as fout:
            fout.write(template)


def load_svg_data():
    # Create timetable objects for the two destinations and have them load the connections
    timetable_frankfurt = Timetable('29fcbcce-2851-4ce3-8c9c-b2a39645cff2', 'Frankfurt West')
    timetable_frankfurt.refresh()
    timetable_giessen = Timetable('29fcbcce-2851-4ce3-8c9c-b2a39645cff2', 'Gießen')
    timetable_giessen.refresh()

    # Combine all the information into a dict
    svg_data = {'clock': datetime.now().strftime('%H:%M')}

    # Todo show no info when not available
    for i in range(0, 2):
        svg_data[f'de_{i}'] = timetable_frankfurt.connections[i].departure.strftime("%H:%M")
        svg_data[f'd_{i}'] = f'+{timetable_frankfurt.connections[i].delay}'

    for i in range(2, 4):
        svg_data[f'de_{i}'] = timetable_giessen.connections[i - 2].departure.strftime("%H:%M")
        svg_data[f'c_{i}'] = str(timetable_giessen.connections[i - 2].train_changes)
        svg_data[f'd_{i}'] = f'+{timetable_giessen.connections[i - 2].delay}'
        svg_data[f'a_{i}'] = ':'.join(str(timetable_giessen.connections[i - 2].duration).split(':')[:2])

    # Load Data into SVG
    create_svg(svg_data, join(svg_path, "template.svg"), join(svg_path, "filled_in.svg"))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "pc":
        svg_path = '/images'

    # https://blog.4dcu.be/diy/2020/09/27/PythonKindleDashboard_1.html
    load_svg_data()
