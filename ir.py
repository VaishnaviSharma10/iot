import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(14,GPIO.IN)
c=0

while 1:
	if(GPIO.input(14)==False): #object is far away
			GPIO.output(2,True)
			print("LED ON")	
			time.sleep(1) 
       
	if(GPIO.input(14)==True): #object is far away
			GPIO.output(2,False)
			print("LED OFF")	
			time.sleep(1) 
			c=c+1
			print(c)
			
