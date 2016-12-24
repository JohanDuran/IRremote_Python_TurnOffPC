import serial
import subprocess
import os
enteroApagar = int("0xFE7887",16)
ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
	lectura = int(ser.readline(),16)
	if lectura == enteroApagar:
		operative = os.name
		if(os.name == 'posix'):
			subprocess.call(["sudo", "shutdown", "-h", "now"])#ubuntu
		else:#in case you just have linux and windows on your machine
			subprocess.call(["shutdown", "/s"])#para windows
