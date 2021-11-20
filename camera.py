import time
from picamera import PiCamera

camera =PiCamera()
time.sleep(2)

camera.capture("/home/pi/Pictures/img2.jpg")
print("done.")
