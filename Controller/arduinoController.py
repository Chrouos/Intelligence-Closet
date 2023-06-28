import serial
from time import sleep
import sys

class ArduinoController:
    
    def __init__(self):
        self.COM_PORT = 'COM4'  # 請自行修改序列埠名稱
        self.BAUD_RATES = 9600
        
    def takeTheClothes_single(self, position):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    ser.write(b'Take_The_Clothes\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Take_The_Clothes] 拿取指令, 單件...')
                    instruction_send_done = True

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Take_The_Clothes] 回應：', mcu_feedback)
                    
                    if "please_input_str_position" in mcu_feedback:
                        msg = str(position) + '\n'
                        ser.write(msg.encode())
                        sleep(0.5)
                        print("[Take_The_Clothes] 收到拿取指令，輸入模塊位置為:", position)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
    def takeTheClothes_second(self, position):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    ser.write(b'Take_The_Clothes_Second\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Take_The_Clothes_Second] 拿取指令, 單件...')
                    instruction_send_done = True

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Take_The_Clothes_Second] 回應：', mcu_feedback)
                    
                    if "please_input_str_position" in mcu_feedback:
                        msg = str(position) + '\n'
                        ser.write(msg.encode())
                        sleep(0.5)
                        print("[Take_The_Clothes_Second] 收到拿取指令，輸入模塊位置為:", position)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
        
    def put_EntranceMidPositionZero(self, position):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    ser.write(b'Put_Entrance_Mid_Position_Zero\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Put_Entrance_Mid_Position_Zero] 入口到位置後歸零...')
                    instruction_send_done = True

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Put_Entrance_Mid_Position_Zero] 回應：', mcu_feedback)
                    
                    if "please_input_str_position" in mcu_feedback:
                        msg = str(position) + '\n'
                        ser.write(msg.encode())
                        sleep(0.5)
                        print("[Put_Entrance_Mid_Position_Zero] 收到存放指令，輸入模塊位置為:", position)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
    def put_EntranceMidPositionZero_second(self, position):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    ser.write(b'Put_Entrance_Mid_Position_Zero_Second\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Put_Entrance_Mid_Position_Zero_Second] 入口到位置後歸零...')
                    instruction_send_done = True

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Put_Entrance_Mid_Position_Zero_Second] 回應：', mcu_feedback)
                    
                    if "please_input_str_position" in mcu_feedback:
                        msg = str(position) + '\n'
                        ser.write(msg.encode())
                        sleep(0.5)
                        print("[Put_Entrance_Mid_Position_Zero_Second] 收到存放指令，輸入模塊位置為:", position)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
    def put_ZeroPositionZero(self, position):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    ser.write(b'Put_Zero_Position_Zero\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Put_Zero_Position_Zero] 歸零到位置放入後回到歸零...')
                    instruction_send_done = True

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Put_Zero_Position_Zero] 回應：', mcu_feedback)
                    
                    if "please_input_str_position" in mcu_feedback:
                        msg = str(position) + '\n'
                        ser.write(msg.encode())
                        sleep(0.5)
                        print("[Put_Zero_Position_Zero] 收到存放指令，輸入模塊位置為:", position)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
        
    def zeroToEntrance(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    ser.write(b'Zero_To_Entrance\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Zero_To_Entrance] 歸零到入口')
                    instruction_send_done = True

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Zero_To_Entrance] 回應：', mcu_feedback)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
    def entranceToZero(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    print('[Entrance_To_Zero] 入口到歸零')
                    ser.write(b'Entrance_To_Zero\n')        # 訊息必須是位元組類型
                    sleep(0.5)                              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    instruction_send_done = True


                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Entrance_To_Zero] 回應：', mcu_feedback)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
    def returnCraneZero(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    ser.write(b'Return_Crane_Zero\n')     # 訊息必須是位元組類型
                    sleep(0.5)                          # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    print('[Return_Crane_Zero] 歸位指令')
                    instruction_send_done = True

                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Return_Crane_Zero] 回應：', mcu_feedback)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
        
    def midToEntrance(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    print('[Mid_To_Entrance] 置中到入口')
                    ser.write(b'Mid_To_Entrance\n')        # 訊息必須是位元組類型
                    sleep(0.5)                              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    instruction_send_done = True


                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Mid_To_Entrance] 回應：', mcu_feedback)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
        
    def EntranceToMid(self):
        ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
        mcu_feedback = 'Reset'
        instruction_send_done = False
        try:
            while mcu_feedback != "Done":
                
                # 收到「Done」後退出
                if 'Done' in str(mcu_feedback):
                    break

                if mcu_feedback != 'Reset' and instruction_send_done == False:
                    print('[Entrance_To_Mid] 入口到置中')
                    ser.write(b'Entrance_To_Mid\n')        # 訊息必須是位元組類型
                    sleep(0.5)                              # 暫停0.5秒，再執行底下接收回應訊息的迴圈
                    mcu_feedback = "Doing"
                    instruction_send_done = True


                while ser.in_waiting:
                    mcu_feedback = ser.readline().decode()  # 接收回應訊息並解碼
                    mcu_feedback = mcu_feedback.replace("\n", "")
                    print('[Entrance_To_Mid] 回應：', mcu_feedback)
                        
        except KeyboardInterrupt:
            print('終止 !')
            
        
        ser.close()
        
        
        
'''

拿取
Take_The_Clothes: take_zero_position_entrance
Put_Entrance_Mid_Position_Zero: put_entrance_position_zero

放入
Take_The_Clothes: take_zero_position_entrance
Entrance_To_Zero: entrance_to_zero
Put_The_Clothes: put_zero_position_zero

'''