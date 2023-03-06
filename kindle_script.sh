# Connect to the kindle via ssh
# https://www.mobileread.com/forums/showthread.php?t=204942
# Toggle USBNetwork to ON, on kindle beforehand
# Kindle User: root;

# Setup kindle network
# sudo ifconfig enxee4900000000 192.168.15.201
# Kindle ssh:
# sshpass -p password ssh root@192.168.15.244

# Copy files to kindle
sshpass -p "password" scp -r /home/finn/Programmieren/Kindle/fahrplan_kindle root@192.168.15.244:/mnt/base-us/extensions

# Login to kindle and execute the start_once.sh script
sshpass - p "password" -ssh root@192.168.15.244 "sh /mnt/base-us/extensions/fahrplan_kindle/bin/start_once.sh"
exit
