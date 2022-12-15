import serial
from time import sleep
import sys

class arduinoController:
    
    def __init__(self):
        COM_PORT = 'COM4'  # 請自行修改序列埠名稱
        BAUD_RATES = 9600
        self.ser = serial.Serial(COM_PORT, BAUD_RATES)
        self.mcu_feedback = "Reset"
    
    def storage(self):
        self.ser.write(b'GO_Storage\n')  # 訊息必須是位元組類型
        sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
        print('傳送存放指令')
        while self.mcu_feedback != "Done" and self.ser.in_waiting:
            mcu_feedback = self.ser.readline().decode()  # 接收回應訊息並解碼
            mcu_feedback = mcu_feedback.replace("\n", "")
            print('控制板回應：', mcu_feedback)

