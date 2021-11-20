import time
import RPi.GPIO as GPIO
from keypad import keypad

import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
 
GPIO.setwarnings(False)
# Initialize
kp = keypad(columnCount = 4) 

def output(n, block_orientation, rotate, inreverse, text):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=n or 1, block_orientation=block_orientation,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=inreverse)
    print(text)
    show_message(device, text, fill="white", font=proportional(CP437_FONT), scroll_delay=00.1)
    time.sleep(1)
    
while True:
        
    print("Please press * key and then enter password")
    # waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
    
    print (digit)
    time.sleep(0.5)
 
    if(digit == '*'):
        print("Enter your 4 Digit password and then press #")
        seq = []
        for i in range(5):
            digit = None
            while digit == None:
                digit = kp.getKey()
                
            print(digit)
            seq.append(digit)
            time.sleep(0.4)
     
        print(seq)
        if seq == [1, 2, 3, 4, '#']:
            print ("Code accepted")
            output(1,0,0,False, "password correct")
        else:
            print("Please try again !")
            output(1,0,0,False, "password wrong")
    else:
        print("Wrong key is Pressed")

