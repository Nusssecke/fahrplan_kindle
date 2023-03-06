#!/bin/sh

cd "$(dirname "$0")"

cd "/mnt/base-us/extensions/fahrplan_kindle/"


# Remove files
if [ -f ./svg/tmp.svg ]; then
    rm ./svg/tmp.svg
fi

if [ -f ./svg/tmp.png ]; then
    rm ./svg/tmp.png
fi

# Run script to download data and generate new SVG file
python3 ./bin/svg_gui.py

# Clear screen
/usr/sbin/eips -c

# Copy rsvg-convert to a share where it can be started
# The shared folder that can be accessed via USB is mounted with the noexec flag,
# copying file to /var/tmp gets around this restriction.
if [ ! -f /var/tmp/rsvg-convert ]; then
    cp -rf ./external/* /var/tmp
fi

# Check if images exists and if it does convert it to PNG and show on screen
if [ -e ./svg/tmp.svg ]; then
    export LD_LIBRARY_PATH=/var/tmp/rsvg-convert-lib:/usr/lib:/lib
    /var/tmp/rsvg-convert --format=png --output=./svg/tmp.png ./svg/tmp.svg > /dev/null 2>&1
    fbink -c -g file=./svg/tmp.png,w=600,h=800,halign=center,valign=center > /dev/null 2>&1
fi

# Make sure the screen is fully loaded before going to sleep
sleep 5

currenttime=$(date +%H:%M)
if [[ "$currenttime" > "05:00" ]] || [[ "$currenttime" < "10:00" ]]; then
    # If the time is between 5 and 10
    # Wait a minute and fetch the data again
    sleep 60
else
    # If not then display a screensaver and sleep until 5
    /usr/bin/eips -g ./svg/sleep.png
	
    echo "" > /sys/class/rtc/rtc1/wakealarm
    Following line contains sleep time in seconds
    echo "+3600" > /sys/class/rtc/rtc1/wakealarm
    # Following line will put device into deep sleep until the alarm above is triggered
    echo mem > /sys/power/state
fi

# Kill self and spawn a new instance
/bin/sh ./bin/start.sh && exit
