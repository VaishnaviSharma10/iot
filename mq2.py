import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(14,GPIO.IN)

while 1:
	value =GPIO.input(14)
	print(value) 
	
	if(GPIO.input(14)==True): 
			GPIO.output(2,True)
			print("LED ON")	
			time.sleep(1) 
       
	if(GPIO.input(14)==False): 
			GPIO.output(2,False)
			print("LED OFF")	
			time.sleep(1) 
			
			
