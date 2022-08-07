
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

### 開發版: Arduino MEGA2560 R3

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

### 伺服馬達: MG90S 金屬齒輪
+ 產品尺寸：22.8 * 12.2 * 28.5mmmm
+ 產品重量：13.6克
+ 工作扭矩：2KG /厘米
+ 反應轉速：0.11秒/60度(4.8V
+ 使用溫度：0℃-55℃
+ 死區設定：5微秒 
+ 插頭類型：JR，FUTABA級 
+ 轉動角度：最大90度
+ 舵機類型：數字舵機 
+ 使用電壓：4.8V

[待參考網址:Arduino筆記(15)：控制伺服馬達 Servo](https://atceiling.blogspot.com/2017/03/arduino.html)

---

## Resource From
[TAIWANIOT](https://www.taiwaniot.com.tw/product/arduino-mega-2560-r3-%E9%96%8B%E7%99%BC%E6%9D%BF-atmega2560-16au/)  
[python serial 模組使用方法](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/466944/)
[使用Python的pySerial模組進行序列通訊：連接電腦與Arduino和MicroPython](https://swf.com.tw/?p=1188)
[電阻計算](https://www.digikey.tw/zh/resources/conversion-calculators/conversion-calculator-resistor-color-code)
[TinkerCAD教程：开关](https://www.youtube.com/watch?v=7MRaNhBQ3Kc)
[Python 及 Firmata](https://medium.com/jeasee%E9%9A%A8%E7%AD%86/python-%E5%8F%8A-firmata-c8d104c1cf00)

書本: Python x Arduino物聯網整合開發實戰


----

## MACHINE NOTE



### 伺服馬達 Servo
```python
from asyncore import write
import serial 
import pyfirmata
from pyfirmata import Arduino, PWM , SERVO

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
board.digital[5].mode = SERVO


value = 0
direct = 1
while True:

    # board.digital[5].write(90)
    if value <= 150 and direct == 1:
        value += 30
    else:
        direct = 0
        
    if value >= 30 and direct == 0:
        value -= 30
    else:
        direct = 1

    writeStatus(5, value, "direct " + str(direct) + " " + str(value))
    # board.digital[5].write(value)

    sleep(2)
    
    # board.digital[13].write(0)

```