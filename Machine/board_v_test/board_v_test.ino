#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
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
const int car_front_btn = 29, car_back_btn = 30;
//步進馬達
Stepper disc_stepper(200, 2, 3, 4, 5); 
const int disc_btn_front = 29, disc_btn_back = 30;
const int relay = 48; // 繼電器


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
    pinMode(car_front_btn, INPUT);
    pinMode(car_back_btn, INPUT);
    pinMode(disc_btn_front, INPUT);
    pinMode(disc_btn_back, INPUT);
    for(int i=0; i<4; i++){
        pinMode(entrance_L298N_car[i], OUTPUT);
    }

    // 雙軸伺服馬達
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_y.attach(biaxial_servo_y_pin);

    // 伺服馬達定位
    biaxial_servo_x.write(0);
    biaxial_servo_y.write(0);
    // 步進馬達
    pinMode(relay, OUTPUT);
    digitalWrite(relay, LOW);
    disc_stepper.setSpeed(30);
    
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

    // 車車 - 前進
    if ( digitalRead(car_front_btn) == HIGH){
        
        mfront(entrance_L298N_car);
        Serial.println("car front. ");
    }

    // 車車 - 後退
    else if ( digitalRead(car_back_btn) == HIGH){
        
        mback(entrance_L298N_car);
        Serial.println("car back. ");
    }
    
    else{
        mstop(entrance_L298N_car);
        Serial.println("car stop. ");

    }
    
    // 圓盤 - 正轉
    if ( digitalRead(disc_btn_front) == HIGH){
        
        // 開始旋轉
        digitalWrite(relay, HIGH); // 把繼電器打開
        disc_stepper.step(20);  //正半圈
        Serial.println("disc front. ");
    }
    // 圓盤 - 反轉
    else if ( digitalRead(disc_btn_back) == HIGH){
        // 開始旋轉
        digitalWrite(relay, HIGH);  // 把繼電器打開
        disc_stepper.step(-20);     //正半圈
        Serial.println("disc back. ");
    }
    else{
        digitalWrite(relay, LOW); // 把繼電器關閉
        Serial.println("disc stop. ");
    }


}

// 步進馬達: 停止
void mstop(int l298n_car[4]) {
    digitalWrite(l298n_car[0], LOW);
    digitalWrite(l298n_car[1], LOW);
    digitalWrite(l298n_car[2], LOW);
    digitalWrite(l298n_car[3], LOW);
}
// 步進馬達: 前進
void mfront(int l298n_car[4]) {
    digitalWrite(l298n_car[0], LOW);
    digitalWrite(l298n_car[1], HIGH);
    digitalWrite(l298n_car[2], LOW);
    digitalWrite(l298n_car[3], HIGH);
}
// 步進馬達: 後退
void mback(int l298n_car[4]) {
    digitalWrite(l298n_car[0], HIGH);
    digitalWrite(l298n_car[1], LOW);
    digitalWrite(l298n_car[2], HIGH);
    digitalWrite(l298n_car[3], LOW);
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
