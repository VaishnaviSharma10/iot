import Adafruit_DHT
import time

pin = 4
sensor = Adafruit_DHT11
while 1:
	try:
		humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
		if humidity is not None and temperature is not None:
			print('temperature ={0:0.1f}*c Humidity={1:0.1f}%'.format(temperature,humidity))
		else:
			print('did not receive any reading from sensor,plz check!!')
	except:
		print("connection failure")


