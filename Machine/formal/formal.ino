#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Wire.h>
#include <Stepper.h>

// LCD, 20/21
LiquidCrystal_I2C lcd(0x27, 16, 4); // I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、2為LCD顯示器大小。
Stepper disc_stepper(200, 2, 3, 4, 5);  // 360 / 120(120步可以轉一圈) = 30(每一步30度)

// ----------------------------------------------- 變數設定 ----------------------------------------------- //

const int tailButton = 22; // 尾巴的微動開關 
const int entranceButton = 24; // 入口的微動開關
const int discButton = 23;  // 圓盤的微動開關
const int entrance_L298N1_In1 = 6; // 車車(減速馬達)的L298N in1
const int entrance_L298N1_In2 = 7; // 車車(減速馬達)的L298N in2 
const int export_L298N1_In3 = 8; // 車車(減速馬達)的L298N in3
const int export_L298N1_In4 = 9; // 車車(減速馬達)的L298N in4
const int trigPin = 40; // 超音波 trig
const int echoPin = 42; // 超音波 echo
const int electromagnet = 45; // 電磁鐵
const int relay = 48; // 繼電器
const int car_servo_pin = A1; // 車車＿伺服馬達 腳位

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

// 車車上的伺服馬達
Servo car_servo;  // create servo object to control a servo

// ----------------------------------------------- 變數設定 ----------------------------------------------- //

void setup() {

    Serial.begin(9600); 

    pinMode(entrance_L298N1_In1, OUTPUT);
    pinMode(entrance_L298N1_In2, OUTPUT);
    pinMode(export_L298N1_In3, OUTPUT);
    pinMode(export_L298N1_In4, OUTPUT);

    pinMode(entranceButton, INPUT);
    pinMode(tailButton, INPUT);
    pinMode(discButton, INPUT);

    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);

    digitalWrite(trigPin, LOW);

    pinMode(relay, OUTPUT);
    digitalWrite(relay, LOW);

    car_servo.attach(car_servo_pin);

    // 步進馬達
    disc_stepper.setSpeed(60);

    // 初始化 LCD
    lcd.init();
    lcd.backlight();

    setUpLCD(1, 0, "stand by now");

    car_servo.write(0); // 初始化鉤子

    Serial.println("----------- 等待指令中 -----------");
}

void loop() {

    
    if (Serial.available()) {
        
        String command = Serial.readStringUntil('\n'); // 收到的指令 // 讀取傳入的字串直到"\n"結尾

        // ---------------- 存放 START---------------- // 
        if (command == "GO_Storage") {
            lcd.clear();
            Serial.println("GO Storage");
            setUpLCD(1, 0, "GO Storage...");

            // 檢視口的車車把伺服馬達鉤子落下
            car_servo.write(90); // 鉤子落下 90度
            delay(2000);
            setUpLCD(1, 1, "Hook: O");
            setUpLCD(1, 2, "Running,  Front");


            // 開始步驟   
            bool start = true; // true: start, false: stop

            // 動作
            Serial.println("等待超音波或微動開關");
            while(start == true){

                mfront(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4); // 馬達前進
                
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
                        mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);

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

                        mfront(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
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
            mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4); // 馬達停下
            setUpLCD(1, 2, "Stopping, Front");


            // 伺服馬達鉤子抬起
            car_servo.write(0);
            setUpLCD(1, 1, "Hook: X");  Serial.println("鉤子抬起");
            delay(2000);

            // 反轉兩秒
            setUpLCD(1, 2, "Running,  Back ");  Serial.println("反轉兩秒");
            motor_back_with_time(2000, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4); 
            setUpLCD(1, 2, "Stopping,  Back");  Serial.println("反轉停止");

            // TODO: 圓盤轉至「位置為無」
            setUpLCD(1, 3, "Disc           " + String(3));  Serial.println("圓盤轉動位置至" + String(3));
            discRotate_withTimes(3); // TODO: 3為測試數值，之後接上資料庫做正確數值修改
            delay(1000);

            // 正轉 ~ 停止
            setUpLCD(1, 2, "Running,  Front");  Serial.println("正轉");
            motor_running(1, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
            setUpLCD(1, 2, "Stopping, Front");  Serial.println("正轉停止");

            // 伺服馬達鉤子落下
            car_servo.write(90); 
            setUpLCD(1, 1, "Hook: O");  Serial.println("鉤子落下");
            delay(2000);

            // 反轉 ~ 停止
            setUpLCD(1, 2, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
            setUpLCD(1, 2, "Stopping,  Back");  Serial.println("反轉停止");

            // 伺服馬達鉤子抬起
            car_servo.write(0);
            setUpLCD(1, 1, "Hook: X");  Serial.println("鉤子抬起");
            delay(2000);

            // 結束步驟            
            lcd.clear();
            setUpLCD(1, 0, "stand by now");

            Serial.println("Done");
        } 
        // ---------------- 存放 END ---------------- //

        // ---------------- 拿取 START---------------- //
        else if (command == "GO_PickUp_1") {
            lcd.clear();

            Serial.println("GO PickUp");
            setUpLCD(1, 0, "GO PickUp 1...");   
            
            // 開始步驟
            Serial.println("Input_The_Position_1");
            String get_position_1 =  Serial.readStringUntil('\n');
            int position_1 = get_position_1.toInt();
            Serial.println("輸入的位置 " + String(position_1));

            // 伺服馬達鉤子落下
            car_servo.write(90); 
            setUpLCD(1, 1, "Hook: O");  Serial.println("鉤子落下"); 
            delay(2000);

            // 正轉 ~ 停止
            setUpLCD(1, 2, "Running,  Front");  Serial.println("正轉兩秒");
            motor_running(1, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
            setUpLCD(1, 2, "Stopping, Front");  Serial.println("正轉停止");

            // 伺服馬達鉤子抬起
            car_servo.write(0);
            setUpLCD(1, 1, "Hook: X");  Serial.println("鉤子抬起");
            delay(2000);

            // 反轉兩秒
            setUpLCD(1, 2, "Running,  Back ");  Serial.println("反轉兩秒");
            motor_back_with_time(2000, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
            setUpLCD(1, 2, "Stopping,  Back");  Serial.println("反轉停止");

            // TODO: 圓盤位置轉至「指定」
            setUpLCD(1, 3, "Disc           " + String(position_1));  Serial.println("圓盤轉動位置至" + String(position_1));
            discRotate_withTimes(position_1); // TODO: 3為測試數值，之後接上資料庫做正確數值修改
            delay(1000);

            // 正轉 ~ 停止
            setUpLCD(1, 2, "Running,  Front");  Serial.println("正轉兩秒");
            motor_running(1, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
            setUpLCD(1, 2, "Stopping, Front");  Serial.println("正轉停止");

             // 伺服馬達鉤子落下
            car_servo.write(90); Serial.println("鉤子落下");
            setUpLCD(1, 1, "Hook: O");
            delay(2000);

            // 反轉 ~ 停止
            setUpLCD(1, 2, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
            setUpLCD(1, 2, "Stopping,  Back");  Serial.println("反轉停止");

            // 伺服馬達鉤子抬起
            car_servo.write(0);
            setUpLCD(1, 1, "Hook: X");  Serial.println("鉤子抬起");
            delay(2000);

            // 結束動作
            lcd.clear();
            setUpLCD(1, 0, "stand by now");

            Serial.println("Done");
        }
        // ---------------- 拿取 END ---------------- //

        // ---------------- 直線到底(前進) START---------------- //
        else if (command == "GO_Straight_Front") {
            Serial.println("GO Straight Front");

            motor_running(1, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
            Serial.println("Done");
        }
        // ---------------- 直線到底(前進) END ---------------- //

        // ---------------- 直線到底(出來) START---------------- //
        else if (command == "GO_Straight_Back") {
            Serial.println("GO Straight Back");

            motor_running(2, entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
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
            setUpLCD(1, 0, "stand by now");
            digitalWrite(relay, LOW); // 繼電器關閉
            Serial.println("Done");
        }
        else{
            Serial.println("Done");
        }

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
void motor_running(int type, int In1, int In2, int In3, int In4){
    bool temp_start = true;  // true: start, false: stop

    while(temp_start == true){

        if(type == 1 ){
            mfront(In1, In2, In3, In4); // 馬達前進
        }
        else if (type == 2){
            mback(In1, In2, In3, In4); // 馬達後退
        }

        // 是否到底(停下)
        if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
        ||  checkTheBtnStatus( tailButton, tailButtonState, tailButtonLastState, tailButtonlastDebounceTime, globalDelayTime) == true
        ){
            Serial.println("GO Storage Button True");
            temp_start = false;
        }
    }
    mstop(In1, In2, In3, In4);
} 

// 反轉兩秒
void motor_back_with_time(int backTime, int In1, int In2, int In3, int In4){
    
    bool backMotor_start = true;
    int backMotor_startTime = millis();
    while(backMotor_start == true){
        
        int backMotor_nowTime = millis(); 
        mback(In1, In2, In3, In4); // 馬達後退

        // 計時兩秒
        if( backMotor_nowTime - backMotor_startTime >= 2000 ){
            backMotor_start = false;
        }
    }
    mstop(In1, In2, In3, In4);
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
