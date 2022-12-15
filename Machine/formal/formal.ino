#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Wire.h>
#include <Stepper.h>


// ----------------------------------------------- 變數設定 v ----------------------------------------------- //

LiquidCrystal_I2C lcd(0x27, 16, 4); // LCD, 20/21, I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、4為LCD顯示器大小。
Stepper disc_stepper(200, 2, 3, 4, 5);  // (200步可以轉一圈) = 1.8度
Servo biaxial_servo_x, biaxial_servo_y; // 機械手臂 伺服馬達
Servo car_servo;    // 車車的伺服馬達

const int tailButton = 22; // 尾巴的微動開關 
const int discButton = 23;  // 圓盤的微動開關
const int entranceButton = 24; // 入口的微動開關

const int biaxial_servo_x_control_btn_positive = 25;
const int biaxial_servo_x_control_btn_negative = 27;
const int biaxial_servo_y_control_btn_positive = 29;
const int biaxial_servo_y_control_btn_negative = 31;
const int car_front_btn = 33;
const int car_back_btn = 35;
const int disc_btn_back = 37;
const int disc_btn_front = 39;

const int entrance_L298N_car[4] = {6, 7, 8, 9};
const int trigPin = 40; // 超音波 trig
const int echoPin = 42; // 超音波 echo
const int relay = 48; // 繼電器
const int biaxial_servo_x_pin = A1, biaxial_servo_y_pin = A2;  // 雙軸: 機械手臂 X, Y軸
const int car_servo_pin = A4;


// ----------------------------------------------- 變數設定 ^ ----------------------------------------------- //

// ----------------------------------------------- 狀態設定 v ----------------------------------------------- //

long globalDelayTime = 50;  // 消斗的時間

int entranceButtonState; // 入口微動開關的狀態
int entranceButtonLastState = LOW; // 入口微動開關的最後狀態
long entranceButtonlastDebounceTime = 0;  // 按了最後一次被觸發

int tailButtonState; // 尾巴微動開關的狀態
int tailButtonLastState = LOW; // 尾巴微動開關的最後狀態
long tailButtonlastDebounceTime = 0;  // 按了最後一次被觸發

int discButtonState; // 圓盤微動開關的狀態
int discButtonLastState = LOW; // 圓盤微動開關的最後狀態
long discButtonlastDebounceTime = 0;  // 按了最後一次被觸發

int Duration; // 超音波發射到接收的時間
int Distance; // 距離
int isTri = true, trigNow = 0, echoNow = 0, isDone = false;

int Y_Track_Up = 150, Y_Track_Down = 0, Y_Disc_Up = 150, Y_Disc_Down = 0;
int X_Track = 0, X_Disc = 130;
int Car_Servo_Up = 165, Car_Servo_Down = 100;
int angle_delayTime = 2000;

// ----------------------------------------------- 狀態設定 ^ ----------------------------------------------- //

void setup() {

    Serial.begin(9600); 

    for(int i = 0; i < 4; i++ ){
        pinMode(entrance_L298N_car[i], OUTPUT);
    }

    pinMode(biaxial_servo_x_control_btn_positive, INPUT);
    pinMode(biaxial_servo_x_control_btn_negative, INPUT);
    pinMode(biaxial_servo_y_control_btn_positive, INPUT);
    pinMode(biaxial_servo_y_control_btn_negative, INPUT);
    pinMode(car_front_btn, INPUT);
    pinMode(car_back_btn, INPUT);
    pinMode(disc_btn_back, INPUT);
    pinMode(disc_btn_front, INPUT);

    pinMode(entranceButton, INPUT);
    pinMode(tailButton, INPUT);
    pinMode(discButton, INPUT);

    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    digitalWrite(trigPin, LOW);

    pinMode(relay, OUTPUT);
    digitalWrite(relay, LOW);

    // 雙軸伺服馬達
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    car_servo.attach(car_servo_pin); 

    // 伺服馬達定位
    biaxial_servo_x.write(0);
    biaxial_servo_y.write(0);
    car_servo.write(Car_Servo_Up);

    // 步進馬達
    disc_stepper.setSpeed(60);

    // 初始化 LCD
    lcd.init();
    lcd.backlight();

    setUpLCD(1, 0, "wait instruction");

    // 最後歸位
    delay(1000);
    biaxial_servo_x.detach();
    biaxial_servo_y.detach();
    car_servo.detach();
    Serial.println("----------- 等待指令中 -----------");
}

void loop() {

    
    if (Serial.available()) {
        
        String command = Serial.readStringUntil('\n'); // 收到的指令 // 讀取傳入的字串直到"\n"結尾

        // ---------------- 存放 START---------------- // 
        if (command == "GO_Storage") {
            lcd.clear();
            Serial.println("GO Storage");
            setUpLCD(1, 0, "GO Storage");
            setUpLCD(1, 2, "Y: Down, X: Track");  


            // 開始步驟 
            bool start = true; // true: start, false: stop

            // 開始動作 - 車子啟動
            Serial.println("等待超音波或微動開關");
            while(start == true){

                mfront(entrance_L298N_car); // 馬達前進
                setUpLCD(1, 1, "Running,  Front ");
                
                // 準備拍照
                if (isTri == true && isDone == false) { // 可發射 且 未完成拍照 (持續發射)
                    digitalWrite(trigPin, HIGH);        // 發射超音波
                    isTri = false;                      // 不可發射
                    trigNow = millis();                 // 計算發射時間(start)
                } else if (isTri == false && millis() - trigNow >= 500) { // 不可發射 且 發射時間大於0.5s (停止發射)
                    isTri = true;                           // 可重新發射了

                    digitalWrite(trigPin, LOW);             // 停止發射超音波
                    Duration = pulseIn(echoPin, HIGH);      // 超音波發射到接收的時間
                    Distance = Duration * 0.034 / 2;        // 計算距離(cm)

                    setUpLCD(1, 3, "Distance " + String(Distance) + "    ");

                    if (Distance <= 20) {                   // 距離小於 20cm
                        Serial.println("超音波感測距離 < 20!!");
                        // 稍微停止一下
                        mstop(entrance_L298N_car);

                        // 拍照
                        Serial.println("Photograph");

                        // 等待5秒
                        int nowTempTime = millis();

                        Serial.println("等待5秒");
                        while (millis() - nowTempTime <= 5000) {
                            setUpLCD(1, 3, + "Waiting ... " + String(5 - int(millis() - nowTempTime) / 1000) +  "  ");
                        }
                        setUpLCD(1, 3, "Not Distance Now");
                        Serial.println("重新啟動 正轉");

                        mfront(entrance_L298N_car);
                        isDone = true;
                        
                    }
                }
                
                // 是否到底(停下)
                if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
                ||  checkTheBtnStatus( tailButton, tailButtonState, tailButtonLastState, tailButtonlastDebounceTime, globalDelayTime) == true
                ){
                    Serial.println("GO Storage Button True");
                    start = false;
                    Serial.println("碰到 微動開關 停止運轉馬達");
                }

            }
            mstop(entrance_L298N_car); // 馬達停下
            setUpLCD(1, 1, "Stopping, Front ");

            // 機械手臂Y軸上升: 提取衣物(軌道)
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂Y軸上升: 提取衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 5, Y_Track_Down, Y_Track_Up);

            delay(1500);

            // 模型車掛臂收回
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            car_servo.attach(car_servo_pin);
            car_servo.write(Car_Servo_Down);
            delay(angle_delayTime);
            car_servo.detach();

            // 反轉 ~ 停止(回到入口)
            setUpLCD(1, 1, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping,  Back");  Serial.println("反轉停止");

            // 模型車掛臂露出
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            car_servo.attach(car_servo_pin);
            car_servo.write(Car_Servo_Up);
            delay(angle_delayTime);
            car_servo.detach();

            // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 15, X_Track, X_Disc);

            // 機械手臂Y軸下降: 放下衣物(圓盤)
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂Y軸下降: 放下衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 5, Y_Disc_Up, Y_Disc_Down);

            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            biaxial_servo_x.attach(biaxial_servo_x_pin);
            biaxial_servo_x.write(X_Track);
            delay(angle_delayTime);
            biaxial_servo_x.detach();

            // TODO: 圓盤轉至「位置為無」
            // setUpLCD(1, 3, "Disc           " + String(3));  Serial.println("圓盤轉動位置至" + String(3));
            // discRotate_withTimes(3); // TODO: 3為測試數值，之後接上資料庫做正確數值修改
            // delay(1000);

            // 結束步驟            
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");

            Serial.println("Done");
        } 
        // ---------------- 存放 END ---------------- //

        // ---------------- 拿取 START---------------- //
        else if (command == "GO_PickUp_1") {
            lcd.clear();

            Serial.println("GO PickUp 1");
            setUpLCD(1, 0, "GO PickUp 1");   
            setUpLCD(1, 2, "Y: Down, X: Track");  

            // 開始步驟
            Serial.println("Input_The_Position_1");
            String get_position_1 =  Serial.readStringUntil('\n');
            int position_1 = get_position_1.toInt();
            Serial.println("輸入的位置 " + String(position_1));

            // TODO: 圓盤轉至「位置指定」

            // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            biaxial_servo_x.attach(biaxial_servo_x_pin);
            biaxial_servo_x.write(X_Disc);
            delay(angle_delayTime);
            biaxial_servo_x.detach();

            // 機械手臂Y軸上升: 提取衣物(圓盤)  
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂Y軸上升: 提取衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 5, Y_Disc_Down, Y_Disc_Up);

            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 10, X_Disc, X_Track);

            // 模型車掛臂收回
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            car_servo.attach(car_servo_pin);
            car_servo.write(Car_Servo_Down);
            delay(angle_delayTime);
            car_servo.detach();

            // 正轉 ~ 停止(進入尾巴)
            setUpLCD(1, 1, "Running,  Front");  Serial.println("正轉至 碰到微動開關為止");
            motor_running(1, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping, Front");  Serial.println("正轉停止");
            
            // 機械手臂Y軸下降: 放下衣物(軌道)
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂Y軸下降: 放下衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 5, Y_Track_Up, Y_Track_Down);

            // 反轉 ~ 停止(回到入口)
            setUpLCD(1, 1, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping,  Back");  Serial.println("反轉停止");

            // 結束動作
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");

            Serial.println("Done");
        }
        // ---------------- 拿取 END ---------------- //

        // ---------------- 直線到底(前進) START---------------- //
        else if (command == "GO_Straight_Front") {
            Serial.println("GO Straight Front");

            motor_running(1, entrance_L298N_car);
            Serial.println("Done");
        }
        // ---------------- 直線到底(前進) END ---------------- //

        // ---------------- 直線到底(出來) START---------------- //
        else if (command == "GO_Straight_Back") {
            Serial.println("GO Straight Back");

            motor_running(2, entrance_L298N_car);
            Serial.println("Done");
        }
        // ---------------- 直線到底(出來) END ---------------- //

        
        else if (command == "GO_Disc"){

            Serial.println("GO_Disc");
            lcd.clear();
            setUpLCD(1, 0, "disc around now");

            // 開始旋轉
            digitalWrite(relay, HIGH); // 把繼電器打開
            bool disc_start = true;  // true: start, false: stop
            while(disc_start == true){
                // stepper_front(disc_L298N1_In1, disc_L298N1_In2, disc_L298N1_In3, disc_L298N1_In4);

                disc_stepper.step(20);  //正半圈

                if( checkTheBtnStatus(discButton, discButtonState, discButtonLastState, discButtonlastDebounceTime, globalDelayTime) == true
                ){
                    Serial.println("GO DISC Button True");
                    disc_start = false;
                }
                if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
                ||  checkTheBtnStatus(tailButton, tailButtonState, tailButtonLastState, tailButtonlastDebounceTime, globalDelayTime) == true
                ){
                    Serial.println("GO DISC Button True");
                    disc_start = false;
                }
            }
            // 微動開關按了才結束

            // 結束
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            digitalWrite(relay, LOW); // 繼電器關閉
            Serial.println("Done");
        }
        else{
            Serial.println("Done");
        }

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
// LCD 顯示畫面
void setUpLCD(int column, int row, String text){
    lcd.setCursor(column, row);  // (colum, row) 
    lcd.print(text);
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

// type = 1: 前進, type = 2: 後退
void motor_running(int type, int l298n_car[4]){
    bool temp_start = true;  // true: start, false: stop

    while(temp_start == true){

        if(type == 1 ){
            mfront(l298n_car); // 馬達前進
        }
        else if (type == 2){
            mback(l298n_car); // 馬達後退
        }

        // 是否到底(停下)
        if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
        ||  checkTheBtnStatus( tailButton, tailButtonState, tailButtonLastState, tailButtonlastDebounceTime, globalDelayTime) == true
        ){
            Serial.println("GO Storage Button True");
            temp_start = false;
        }
    }
    mstop(l298n_car);
} 


void discRotate_withTimes(int times){

    Serial.println("discRotate_withTimes have to rotate " + String(times) + " Times");

    // 開始旋轉
    digitalWrite(relay, HIGH); // 把繼電器打開
    int nowTimes = 0;
    bool disc_start = true;  // true: start, false: stop
    while(disc_start == true){
        // stepper_front(disc_L298N1_In1, disc_L298N1_In2, disc_L298N1_In3, disc_L298N1_In4);

        disc_stepper.step(20);  // 20 / 200 = 1 / 10,  360 * 0.1 = 3.6(度)

        if( checkTheBtnStatus(discButton, discButtonState, discButtonLastState, discButtonlastDebounceTime, globalDelayTime) == true
        ){
            Serial.println("-- Now Rotate Times: " + String(nowTimes));
            nowTimes++;
        }
        
        if( nowTimes >= times) disc_start = false;
    }
    digitalWrite(relay, LOW); // 把繼電器關閉

    // 微動開關按了指定「次數」才結束
}

void servo_with_time(Servo servo_now, int servo_pin, int speed, int angle_now, int angle_need){
    servo_now.attach(servo_pin);
    
    for( int i = angle_now; i <= angle_need; i += speed ){
        servo_now.write(angle_now);
        delay(15);
    }
    
    // 結束連線
    delay(angle_delayTime);
    servo_now.detach();
}