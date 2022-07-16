import serial 
import pyfirmata
from time import sleep

def blinkLED(pin, status, message):
    print(message)
    board.digital[pin].write(status) # HIGH: 1
    
    
port = "COM3"
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

status = 1
while True:
    
    if status == 1:
        blinkLED(13, 1, "blink")
        status = 0
        
    elif status == 0: 
      blinkLED(13, 0, "dark now")
      status = 1    
           
    sleep(1)
        


