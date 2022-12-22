import serial
from time import sleep
import sys

class ArduinoController:
    
    def __init__(self):
        self.COM_PORT = 'COM4'  # 請自行修改序列埠名稱
        self.BAUD_RATES = 9600
        
    
    def storage(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        try:
            sleep(1)
            while mcu_feedback != "Done":
                
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback == 'Reset':
                    print('傳送存放指令')
                    ser.write(b'GO_Storage\n')  # 訊息必須是位元組類型
                    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('控制板回應：', mcu_feedback)
        except KeyboardInterrupt:
            print('再見！')
            
        ser.close()
        
        
    def pickUp_one_clothes(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        try:
            sleep(1)
            while mcu_feedback != "Done":
                
                if 'Done' in str(mcu_feedback):
                    break
                
                if mcu_feedback == 'Reset':
                    print('傳送存放指令')
                    ser.write(b'GO_Storage\n')  # 訊息必須是位元組類型
                    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('控制板回應：', mcu_feedback)
        except KeyboardInterrupt:
            print('再見！')
            
        ser.close()
        
    def storgage_first_half(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        try:
            sleep(1)
            while mcu_feedback != "Done":
                
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback == 'Reset':
                    print('傳送存放指令 前半部')
                    ser.write(b'GO_TakeAPhoto_S1\n')  # 訊息必須是位元組類型
                    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('控制板回應：', mcu_feedback)
        except KeyboardInterrupt:
            print('再見！')
            
        ser.close()
            
    def storgage_second_half(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        try:
            sleep(1)
            while mcu_feedback != "Done":
                
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback == 'Reset':
                    print('傳送存放指令 後半部')
                    ser.write(b'GO_Storage_S2\n')  # 訊息必須是位元組類型
                    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('控制板回應：', mcu_feedback)
        except KeyboardInterrupt:
            print('再見！')
            
        ser.close()   
    
    def car_back_now(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        try:
            sleep(1)
            while mcu_feedback != "Done":
                
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback == 'Reset':
                    print('傳送回來指令')
                    ser.write(b'GO_Straight_Back\n')  # 訊息必須是位元組類型
                    sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('控制板回應：', mcu_feedback)
        except KeyboardInterrupt:
            print('再見！')
            
        ser.close()

'''

COM_PORT = 'COM4'
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
mcu_feedback = 'Done'
choice = 'nothing'


try:
    while True:
        # 接收用戶的輸入值並轉成小寫
        if 'Done' in str(mcu_feedback):
            choice = input('按1存放、按2拿出、按3轉圈，按e關閉程式  ').lower()
            mcu_feedback = "Reset"

        if choice == '1':
            print('傳送存放指令')
            ser.write(b'GO_Storage\n')  # 訊息必須是位元組類型
            sleep(0.5)  # 暫停0.5秒，再執行底下接收回應訊息的迴圈
        elif choice == '2':
            print('傳送拿取指令')
            ser.write(b'GO_PickUp_1\n')
            sleep(0.5)
        elif choice == '3':
            print('傳送轉圈指令')
            ser.write(b'GO_Disc\n')
            sleep(0.5)
        elif choice == '4':
            print('傳送衝到底指令')
            ser.write(b'GO_Straight_Front\n')
            sleep(0.5)
        elif choice == '5':
            print('傳送衝回來指令')
            ser.write(b'GO_Straight_Back\n')
            sleep(0.5)
        elif choice == 'e':
            ser.close()
            print('再見！')
            sys.exit()
        elif choice == 'nothing':
            sleep(0.5)
        else:
            print('指令錯誤…')
            mcu_feedback = "Done"

        while ser.in_waiting:
            choice = 'nothing'
            mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
            mcu_feedback = mcu_feedback.replace("\n", "")
            print('控制板回應：', mcu_feedback)

            if "Photograph" in mcu_feedback:
                print("拍個照片")
            
            if "Input_The_Position_1" in mcu_feedback:
                position_1 = 2
                msg = str(position_1) + '\n'
                ser.write(msg.encode())
                sleep(0.5)
                print("拿取位置", position_1, "的衣服")

except KeyboardInterrupt:
    ser.close()
    print('再見！')
'''
