import RPi.GPIO as GPIO
import time


servo_pin= 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

pwm=GPIO.PWM(servo_pin,50)# 50hz frequency

pwm.start(7)
for i in range(0,3):
	pwm.ChangeDutyCycle(2.0) #rotate to 0 degrees
	time.sleep(0.5)
	pwm.ChangeDutyCycle(12.0) #rotate to 180 degree
	time.sleep(0.5)
	pwm.ChangeDutyCycle(7.0) #rotate to 90 degree
	time.sleep(0.5)
	
pwm.ChangeDutyCycle(0)  #this is present jitter
pwm.stop()
GPIO.cleanup()
