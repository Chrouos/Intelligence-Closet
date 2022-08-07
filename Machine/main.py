import serial 
import pyfirmata
from time import sleep

def writeStatus(pin, status, message):
    board.digital[pin].write(status) # HIGH: 1
    print(message)

def readStatus(pin, message):
    signal = board.digital[pin].read()
    print(message, signal)
    
# 連接的PORT
port = "COM3"
board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start()

### 開始

## 腳位

mydelay = 1
while True:
    
    writeStatus(4, 1, "1")    
    writeStatus(5, 1, "1")    
    writeStatus(6, 0, "1")
    writeStatus(7, 0, "1")
    sleep(mydelay)
    
    writeStatus(4, 0, "2")    
    writeStatus(5, 1, "2")    
    writeStatus(6, 1, "2")
    writeStatus(7, 0, "2")
    sleep(mydelay)
    
    writeStatus(4, 0, "3")    
    writeStatus(5, 0, "3")    
    writeStatus(6, 1, "3")
    writeStatus(7, 1, "3")
    sleep(mydelay)
    
    writeStatus(4, 1, "4")    
    writeStatus(5, 0, "4")    
    writeStatus(6, 0, "4")
    writeStatus(7, 1, "7 0")
    sleep(mydelay)