.PHONY: compose down test python mongo drop

MAKEPATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PWD := $(dir $(MAKEPATH))

run:
	python3 main.py

test:
	python3 test.py

moisture-calibration:
	python3 moisture-calibration.py

test3:
	python3 test3.py

install :
	pip3 install -r dependencies.txt

sync:
	sshpass -p 123qwe rsync -av --exclude '*.git' --exclude '.idea' . pi@hydrosys4-pi:/home/pi/python-pi