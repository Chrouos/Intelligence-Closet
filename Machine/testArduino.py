import serial
from time import sleep
import sys

COM_PORT = 'COM3'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
choice = 'nothing'
mcu_feedback = 'Done'
try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        if 'Done' in str(mcu_feedback):
            choice = input('按1存放、按2拿出、按e關閉程式  ').lower()
            mcu_feedback = "Reset"

        if choice == '1':
            print('傳送存放指令')
            ser.write(b'GO_Storage\n')  # 訊息必須是位元組類型
            sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
        elif choice == '2':
            print('傳送拿取指令')
            ser.write(b'GO_PickUp\n')
            sleep(0.5)
        elif choice == 'e':
            ser.close()
            print('再見！')
            sys.exit()
        elif choice == 'nothing':
            sleep(0.5)
        else:
            print('指令錯誤…')

        while ser.in_waiting:
            choice = 'nothing'
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            mcu_feedback = mcu_feedback.replace("\n", "")
            print('控制板回應：', mcu_feedback)

            if "Photograph" in mcu_feedback:
                print("拍個照片")

except KeyboardInterrupt:
    ser.close()
    print('再見！')