#!/bin/sh
export LD_LIBRARY_PATH=./
while true; do
	mosquitto=`ps aux | grep "mosquitto -p 1884" | grep -v grep`
	main=`ps aux | grep ./main.py | grep -v grep`
	if [ ! "$mosquitto" ]; then
		mosquitto -p 1884 1>>./log/journalMos 2>&1 &
	fi
	if [ ! "$main" ]; then
		python ./main.py 1>>./log/journalMain 2>&1 &
	fi
	sleep 10
done

#sudo nano /etc/systemd/system/alois.service
# [Unit]
# Description=My service
# After=network.target

# [Service]
# ExecStart=/bin/bash /home/pi/Desktop/OCS-2019-master/python/onboot.sh
# WorkingDirectory=/home/pi/Desktop/OCS-2019-master/python/
# StandardOutput=inherit
# StandardError=inherit
# Restart=always
# User=pi

# [Install]
# WantedBy=multi-user.target
# sudo systemctl enable alois.service

