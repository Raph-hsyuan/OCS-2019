#!/bin/sh
export LD_LIBRARY_PATH=./
while true; do
	mosquitto=`ps aux | grep mosquitto | grep -v grep`
	main=`ps aux | grep python | grep -v grep`
	if [ ! "$mosquitto" ]; then
		mosquitto -p 1884 1>>./log/journalMos 2>&1 &
	fi
	if [ ! "$main" ]; then
		python ./main.py 1>>./log/journalMain 2>&1 &
	fi
	sleep 10
done
#sudo nano /etc/rc.local
#before exit 0 add su pi -c "exec /home/pi/Desktop/OCS-2019-master/python/onboot.sh" 
