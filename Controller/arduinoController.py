import serial
from time import sleep
import sys

class ArduinoController:
    
    def __init__(self):
        self.COM_PORT = 'COM4'  # 請自行修改序列埠名稱
        self.BAUD_RATES = 9600
        
    def putClothes(self, put_position):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                # 初始化，送出指令執行指令 「Put_The_Clothes」
                if mcu_feedback == 'Reset':
                    ser.write(b'Put_The_Clothes\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Put_The_Clothes] 存放指令')

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Put_The_Clothes] 回應：', mcu_feedback)
                    
                    if "please_input_str_put_position" in mcu_feedback:
                        position = put_position
                        msg = str(position) + '\n'
                        ser.write(msg.encode())
                        sleep(0.5)
                        print("[Put_The_Clothes] 收到存放指令，輸入存放衣物位置為:", position)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
    def takeClothes_single(self, take_position):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                # 初始化，送出指令執行指令 Take_The_Clothes
                if mcu_feedback == 'Reset':
                    ser.write(b'Take_The_Clothes\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Take_The_Clothes] 拿取指令, 單件...')

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Take_The_Clothes] 回應：', mcu_feedback)
                    
                    if "please_input_str_take_position" in mcu_feedback:
                        position = take_position
                        msg = str(position) + '\n'
                        ser.write(msg.encode())
                        sleep(0.5)
                        print("[Take_The_Clothes] 收到存放指令，輸入存放衣物位置為:", position)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()