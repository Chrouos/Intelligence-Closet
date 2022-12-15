#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Wire.h>
#include <Stepper.h>

// 雙軸伺服馬達
Servo biaxial_servo_x, biaxial_servo_y; 
const int biaxial_servo_x_pin = A1, biaxial_servo_y_pin = A2; 

// ----------------------------- 控制腳位 start ----------------------------- //

// 伺服馬達
const int biaxial_servo_x_control_btn_negative = 26, biaxial_servo_x_control_btn_positive = 25;
const int biaxial_servo_y_control_btn_negative = 28, biaxial_servo_y_control_btn_positive = 27;
// 車車(減速馬達)的L298N
const int entrance_L298N_car[4] = {6, 7, 8, 9};

// ----------------------------- 控制腳位 end ----------------------------- //

// ----------------------------------------------- 變數設定 ----------------------------------------------- //

void setup() {

    // 開啟Serial Port 並設定通訊速率(baud rate) 
    Serial.begin(9600); 

    // 控制腳位
    pinMode(biaxial_servo_x_control_btn_negative, INPUT);
    pinMode(biaxial_servo_x_control_btn_positive, INPUT);
    pinMode(biaxial_servo_y_control_btn_negative, INPUT);
    pinMode(biaxial_servo_y_control_btn_positive, INPUT);

    // 雙軸伺服馬達
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_y.attach(biaxial_servo_y_pin);

    // 伺服馬達定位
    biaxial_servo_x.write(0);
    biaxial_servo_y.write(0);
    
    
    // 最後歸位
    delay(1000);
    biaxial_servo_x.detach();
    biaxial_servo_y.detach();

}

int servo_x_pos = 0, servo_y_pos = 0;
int angle = 1, angle_delayTime = 15;
void loop() {
    

    // x軸 - 負
    if ( digitalRead(biaxial_servo_x_control_btn_negative) == HIGH){
        
        // 按著就增加 angle度
        if(servo_x_pos + (-1 * angle) >= 0 ){
            servo_x_pos += (-1 * angle);
            biaxial_servo_x.attach(biaxial_servo_x_pin);
            biaxial_servo_x.write(servo_x_pos);
            delay(angle_delayTime);
            biaxial_servo_x.detach();
        }

        Serial.println("servo_x_pos: " + String(servo_x_pos));

    }

    // x軸 - 正
    if ( digitalRead(biaxial_servo_x_control_btn_positive) == HIGH){
        
        // 按著就增加 angle度
        if(servo_x_pos + (1 * angle) <= 180 ){
            servo_x_pos += (1 * angle);
            biaxial_servo_x.attach(biaxial_servo_x_pin);
            biaxial_servo_x.write(servo_x_pos);
            delay(angle_delayTime);
            biaxial_servo_x.detach();
        }

        Serial.println("servo_x_pos: " + String(servo_x_pos));

    }

    // y軸 - 負
    if ( digitalRead(biaxial_servo_y_control_btn_negative) == HIGH){
        
        // 按著就增加 angle度
        if(servo_y_pos + (-1 * angle) >= 0 ){
            servo_y_pos += (-1 * angle);
            biaxial_servo_y.attach(biaxial_servo_y_pin);
            biaxial_servo_y.write(servo_y_pos);
            delay(angle_delayTime);
            biaxial_servo_y.detach();
        }

        Serial.println("servo_y_pos: " + String(servo_y_pos));

    }

    // y軸 - 正
    if ( digitalRead(biaxial_servo_y_control_btn_positive) == HIGH){
        
        // 按著就增加 angle度
        if(servo_y_pos + (1 * angle) <= 180 ){
            servo_y_pos += (1 * angle);
            biaxial_servo_y.attach(biaxial_servo_y_pin);
            biaxial_servo_y.write(servo_y_pos);
            delay(angle_delayTime);
            biaxial_servo_y.detach();
        }

        Serial.println("servo_y_pos: " + String(servo_y_pos));

    }
    


}

// 步進馬達: 停止
void mstop(int In1, int In2, int In3, int In4) {
    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
}
// 步進馬達: 前進
void mfront(int In1, int In2, int In3, int In4) {
    digitalWrite(In1, LOW);
    digitalWrite(In2, HIGH);
    digitalWrite(In3, LOW);
    digitalWrite(In4, HIGH);
}
// 步進馬達: 後退
void mback(int In1, int In2, int In3, int In4) {
    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    digitalWrite(In3, HIGH);
    digitalWrite(In4, LOW);
}

// 確認按鈕狀況
int checkTheBtnStatus(const int button, int& buttonState, int& buttonLastState, long& buttonlastDebounceTime, long delayTime){
    int buttonRead = digitalRead(button);
    if (buttonRead != buttonLastState) {  // 如果按键状态和上次不同
        buttonlastDebounceTime = millis();  // 记录初始时间
    }

    if ((millis() - buttonlastDebounceTime) > delayTime) {
        if (buttonRead != buttonState) {  // 如果按键状态改变了
            buttonState = buttonRead;

            // 切換了開始
            if (buttonRead == HIGH) {
                return true;
            }
        }
    }
    buttonLastState = buttonRead;  // 保存处理结果
    return false;
}


                
void stepper_front(int In1, int In2, int In3, int In4) {

    int t = 2;

    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, HIGH);
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    digitalWrite(In3, HIGH);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    digitalWrite(In3, LOW);
    digitalWrite(In4, HIGH);
    delay(t);

}
