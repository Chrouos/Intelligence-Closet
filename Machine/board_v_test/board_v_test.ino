#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Stepper.h>

// 雙軸伺服馬達
Servo biaxial_servo_x, biaxial_servo_y; 
const int biaxial_servo_x_pin = A1, biaxial_servo_y_pin = A2; 
// 車車的伺服馬達
Servo car_servo;
const int car_servo_pin = A4;
// LCD
LiquidCrystal_I2C lcd(0x27, 16, 4); // I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、2為LCD顯示器大小。

// ----------------------------- 控制腳位 start ----------------------------- //

// 伺服馬達
const int biaxial_servo_x_control_btn_negative = 27, biaxial_servo_x_control_btn_positive = 25;
const int biaxial_servo_y_control_btn_negative = 31, biaxial_servo_y_control_btn_positive = 29;
int servo_x_lastStatus = false, servo_y_lastStatus = false;
// 車車(減速馬達)的L298N
const int entrance_L298N_car[4] = {6, 7, 8, 9};
const int car_front_btn = 33, car_back_btn = 35;
int car_lastState = false;
//步進馬達
Stepper disc_stepper(200, 2, 3, 4, 5); 
const int disc_btn_front = 24, disc_btn_stop = 23;
const int relay = 48; // 繼電器
int disc_lastState = false;
// 車車的伺服馬達(掛勾)
const  int car_servo_btn_negative = 39, car_servo_btn_positive = 37;
int car_servo_lastStatus = false;

int servo_x_pos = 0, servo_y_pos = 0, servo_car_pos = 165;
int angle = 1, angle_delayTime = 15;

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

    pinMode(car_servo_btn_negative, INPUT);
    pinMode(car_servo_btn_positive, INPUT);
    pinMode(disc_btn_front, INPUT);
    pinMode(disc_btn_stop, INPUT);
    
    for(int i=0; i<4; i++){
        pinMode(entrance_L298N_car[i], OUTPUT);
    }

    // 伺服馬達
    biaxial_servo_x.attach(biaxial_servo_x_pin); // 雙軸 X
    biaxial_servo_y.attach(biaxial_servo_y_pin); // 雙軸 Y
    car_servo.attach(car_servo_pin); 
    // 伺服馬達定位
    biaxial_servo_x.write(0);
    biaxial_servo_y.write(0);
    car_servo.write(servo_car_pos);

    // 步進馬達
    pinMode(relay, OUTPUT);
    digitalWrite(relay, LOW);
    disc_stepper.setSpeed(10);

    // 初始化 LCD
    lcd.init();
    lcd.backlight();
    lcd.clear();

    setUpLCD(1, 3, "test mode");
    
    
    // 最後歸位
    delay(1000);
    biaxial_servo_x.detach();
    biaxial_servo_y.detach();
    car_servo.detach();

}

void loop() {
//    if ( digitalRead(biaxial_servo_x_control_btn_negative) == HIGH){
//      Serial.println(biaxial_servo_x_control_btn_negative);
//    }
//    if ( digitalRead(biaxial_servo_x_control_btn_positive) == HIGH){
//      Serial.println(biaxial_servo_x_control_btn_positive);
//    }
//    if ( digitalRead(biaxial_servo_y_control_btn_negative) == HIGH){
//      Serial.println(biaxial_servo_y_control_btn_negative);
//    }
//    if ( digitalRead(biaxial_servo_y_control_btn_positive) == HIGH){
//      Serial.println(biaxial_servo_y_control_btn_positive);
//    }
//    if ( digitalRead(car_front_btn) == HIGH){
//      Serial.println(car_front_btn);
//    }
//    if ( digitalRead(car_back_btn) == HIGH){
//      Serial.println(car_back_btn);
//    }
//     if ( digitalRead(disc_btn_front) == HIGH){
//      Serial.println(disc_btn_front);
//    }
//     if ( digitalRead(disc_btn_back) == HIGH){
//      Serial.println(disc_btn_back);
//    }

    // x軸 - 負
    if ( digitalRead(biaxial_servo_x_control_btn_negative) == HIGH){
        
        // 按著就增加 angle度
        if(servo_x_pos + (-1 * angle) >= 0 ){
            servo_x_pos += (-1 * angle);
            biaxial_servo_x.attach(biaxial_servo_x_pin);
            biaxial_servo_x.write(servo_x_pos);
            delay(angle_delayTime);
        }

        Serial.println("servo_x_pos: " + String(servo_x_pos));
        setUpLCD(1, 0, "X: "  + String(servo_x_pos) + " ");
        servo_x_lastStatus = true;
    }
    // x軸 - 正
    else if ( digitalRead(biaxial_servo_x_control_btn_positive) == HIGH){
        
        // 按著就增加 angle度
        if(servo_x_pos + (1 * angle) <= 180 ){
            servo_x_pos += (1 * angle);
            biaxial_servo_x.attach(biaxial_servo_x_pin);
            biaxial_servo_x.write(servo_x_pos);
            delay(angle_delayTime);
        }

        Serial.println("servo_x_pos: " + String(servo_x_pos));
        setUpLCD(1, 0, "X: "  + String(servo_x_pos) + " ");

        servo_x_lastStatus = true;
    }
    else if (servo_x_lastStatus == true 
                && digitalRead(biaxial_servo_x_control_btn_negative) == LOW
                && digitalRead(biaxial_servo_x_control_btn_positive) == LOW){
        biaxial_servo_x.detach();
        servo_x_lastStatus = false;
    }

    // y軸 - 負
    if ( digitalRead(biaxial_servo_y_control_btn_negative) == HIGH){
        
        // 按著就增加 angle度
        if(servo_y_pos + (-1 * angle) >= 0 ){
            servo_y_pos += (-1 * angle);
            biaxial_servo_y.attach(biaxial_servo_y_pin);
            biaxial_servo_y.write(servo_y_pos);
            delay(angle_delayTime);
        }

        Serial.println("servo_y_pos: " + String(servo_y_pos));
        setUpLCD(1, 1, "Y: "  + String(servo_y_pos) + " ");

        servo_y_lastStatus = true;
    }
   // y軸 - 正
    else if ( digitalRead(biaxial_servo_y_control_btn_positive) == HIGH){
        
        // 按著就增加 angle度
        if(servo_y_pos + (1 * angle) <= 180 ){
            servo_y_pos += (1 * angle);
            biaxial_servo_y.attach(biaxial_servo_y_pin);
            biaxial_servo_y.write(servo_y_pos);
            delay(angle_delayTime);
        }

        Serial.println("servo_y_pos: " + String(servo_y_pos));
        setUpLCD(1, 1, "Y: "  + String(servo_y_pos) + " ");

        servo_y_lastStatus = true;
    }
    else if (servo_y_lastStatus == true 
                && digitalRead(biaxial_servo_y_control_btn_negative) == LOW
                && digitalRead(biaxial_servo_y_control_btn_positive) == LOW){
        biaxial_servo_y.detach();
        servo_y_lastStatus = false;
    }

    // 車車 - 前進
    if ( digitalRead(car_front_btn) == HIGH){
        
        mfront(entrance_L298N_car);
        Serial.println("car front. ");
        car_lastState = true;
    }
    // 車車 - 後退
    else if ( digitalRead(car_back_btn) == HIGH){
        
        mback(entrance_L298N_car);
        Serial.println("car back. ");
        car_lastState = true;
    }
    else if(car_lastState == true && digitalRead(car_back_btn) == LOW && digitalRead(car_front_btn) == LOW){
        mstop(entrance_L298N_car);
        car_lastState = false;
    }

  

   // 車車伺服馬達 - 負
    if ( digitalRead(car_servo_btn_negative) == HIGH){
        
        // 按著就增加 angle度
        if(servo_car_pos + (-1 * angle) >= 0 ){
            servo_car_pos += (-1 * angle);
            car_servo.attach(car_servo_pin);
            car_servo.write(servo_car_pos);
            delay(angle_delayTime);
        }

        Serial.println("servo_car_pos: " + String(servo_car_pos));
        setUpLCD(1, 2, "car: "  + String(servo_car_pos) + " ");
        car_servo_lastStatus = true;
    }
    // 車車伺服馬達 - 正
    else if ( digitalRead(car_servo_btn_positive) == HIGH){
        
        // 按著就增加 angle度
        if(servo_car_pos + (1 * angle) <= 180 ){
            servo_car_pos += (1 * angle);
            car_servo.attach(car_servo_pin);
            car_servo.write(servo_car_pos);
            delay(angle_delayTime);
        }

        Serial.println("servo_car_pos: " + String(servo_car_pos));
        setUpLCD(1, 2, "car: "  + String(servo_car_pos) + " ");

        car_servo_lastStatus = true;
    }
    else if (car_servo_lastStatus == true 
                && digitalRead(car_servo_btn_negative) == LOW
                && digitalRead(car_servo_btn_positive) == LOW){
        car_servo.detach();
        car_servo_lastStatus = false;
    }

    if ( digitalRead(disc_btn_front) == HIGH){
        long temp_time = millis();

        // 開始旋轉 
        digitalWrite(relay, HIGH); // 把繼電器打開
        bool disc_start = true;  // true: start, false: stop
        while(disc_start == true){
          
            disc_stepper.step(-1);  // 20/200 = 1/10
            if(millis() - temp_time > 1000){
              if( digitalRead(disc_btn_stop) == true){
                  disc_start = false;
              }
            }
            
        }
        // 微動開關按了才結束

        // 結束
        delay(2000);
        digitalWrite(relay, LOW);
        
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



// LCD 顯示畫面
void setUpLCD(int column, int row, String text){
    lcd.setCursor(column, row);  // (colum, row) 
    lcd.print(text);
}
