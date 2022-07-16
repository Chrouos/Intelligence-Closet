
# Machine

## Python In Arduino
+ 連接Ardino與Python
  1. Arduino's Firmata 通尋協定  
    Find: Arduino IDE -> Example -> Firmata -> StandardFirmata  
    Execute: Upload
  2. Python序列函式庫 pySerial   
     Install pySeria
     ```
     pip install pyserial
     pip install pyfirmata
     ```

### Start to test the example
```python
import serial 

s = serial.Serial('COM3', 9600, timeout=0.5)
if not s.isOpen():
    s.open()
    
print('com3 is open', s.isOpen())
```

```python
import pyfirmata

# Arudino Setting
pin = 13
port = "COM3"

# coding
board = pyfirmata.Arduino(port)
board.digital[pin].write(1) # HIGH: 1
board.digital.pin(0) # LOW: 0
board.digital[pin].read() # READ: 讀取狀態

```

---
## Components
所有在ICLoset中會用到個零件筆記

### Arduino MEGA2560 R3

+ 主控芯片：ATmega2560
+ 工作電壓：5v（USB線供電）
+ 外接電源：7-12V，建議9V
+ 數字輸入輸出口：54個，其中15個支持pwm
+ 模擬輸入輸出口：16個
+ 每個I/O口的輸出電流：40mA
+ 3.3V管腳的輸出電流：50mA
+ 閃存空間：256KB（其中8KB用於加載程序）
+ SRAM：8KB
+ EEPROM：4KB
+ 時鐘頻率：16MHZ

---

## Resource From
[TAIWANIOT](https://www.taiwaniot.com.tw/product/arduino-mega-2560-r3-%E9%96%8B%E7%99%BC%E6%9D%BF-atmega2560-16au/)  
[python serial 模組使用方法](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/466944/)

