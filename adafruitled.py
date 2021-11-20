#pip3 install adafruit-io

import time
import RPi.GPIO as GPIO
from Adafruit_IO import Client

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)


ADAFRUIT_IO_USERNAME = "radhika_more"
ADAFRUIT_IO_KEY = "aio_vuBT34MepYFekeZR1vfLY7o2mtre"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
distance_feed = aio.feeds('light1')
distance_feed = aio.feeds('light2')


while True:
	print("Receiving data..")
	status = aio.receive(distance_feed.key).value
	print(status)
	if status == "ON":
		GPIO.output(3,True)
		print("LED1 ON")
	else:
		GPIO.output(3,False)
		print("LED1 OFF")
	time.sleep(0.1)
	

	print("Receiving data..")
	status = aio.receive(distance_feed.key).value
	print(status)
	if status == "ON":
		GPIO.output(4,True)
		print("LED2 ON")
	else:
		GPIO.output(4,False)
		print("LED2 OFF")
	time.sleep(0.1)
