.PHONY: compose down test python mongo drop

MAKEPATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PWD := $(dir $(MAKEPATH))

run:
	python3 main.py

moisture:
	python3 test_moisture.py

moisture-calibration:
	python3 moisture-calibration.py

test3:
	python3 test3.py

test-pump:
	python3 test_pump.py

install :
	pip3 install -r dependencies.txt

sync:
	sshpass -p 123qwe rsync -av --exclude '*.git' --exclude '.idea' . pi@192.168.0.47:/home/pi/python-pi

ssh:
	sshpass -p 123qwe ssh pi@192.168.0.47

pull-log:
	sshpass -p 123qwe scp pi@192.168.0.47:/tmp/humidity.log /home/pablo/humidity.log
