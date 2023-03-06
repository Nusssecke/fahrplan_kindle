sshpass -p "password" scp -r /home/finn/Programmieren/Kindle/fahrplan_kindle root@192.168.15.244:/mnt/base-us/extensions
sshpass -p "password" ssh root@192.168.15.244 "python3 /mnt/base-us/extensions/fahrplan_kindle/bin/testing.py"
