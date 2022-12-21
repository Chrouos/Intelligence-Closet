import serial
from time import sleep
import sys

COM_PORT = 'COM4'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
choice = 'nothing'
mcu_feedback = 'Reset'

try:
    sleep(1)
    while mcu_feedback != "Done":

        if mcu_feedback == 'Reset':
            print('傳送存放指令')
            ser.write(b'GO_Storage\n')  # 訊息必須是位元組類型
            sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
            mcu_feedback = "Doing"

        while ser.in_waiting:
            choice = 'nothing'
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            mcu_feedback = mcu_feedback.replace("\n", "")
            print('控制板回應：', mcu_feedback)
except KeyboardInterrupt:
    ser.close()
    print('再見！')