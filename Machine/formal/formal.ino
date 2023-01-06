#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Wire.h>
#include <Stepper.h>


// ----------------------------------------------- 變數設定 v ----------------------------------------------- //

LiquidCrystal_I2C lcd(0x27, 16, 4);     // LCD, 20/21, I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、4為LCD顯示器大小。
Stepper disc_stepper(200, 2, 3, 4, 5);  // (200步可以轉一圈) = 1.8度
Servo biaxial_servo_x, biaxial_servo_y; // 機械手臂 伺服馬達
Servo car_servo;                        // 車車的伺服馬達
Servo entrance_servo;                   // 入口的伺服馬達

const int tailButton = 22;      // 尾巴的微動開關 
const int discButton = 23;      // 圓盤的微動開關  
const int entranceButton = 24;  // 入口的微動開關
const int camaraButton = 25;    // 拍照點的微動開關


const int entrance_L298N_car[4] = {6, 7, 8, 9};                 // 模型車的減速馬達
const int relay = 48;                                           // 繼電器
const int biaxial_servo_x_pin = A1, biaxial_servo_y_pin = A2;   // 雙軸: 機械手臂 X, Y軸
const int car_servo_pin = A6, entrance_servo_pin = A5;          // 車子的伺服馬達, 入口的伺服馬達(停車場)


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

int camaraButtonState; // 拍照點的微動開關的狀態
int camaraButtonLastState = LOW; // 拍照點的微動開關的最後狀態
long camaraButtonlastDebounceTime = 0;  // 拍照點的按了最後一次被觸發

// int Duration; // 超音波發射到接收的時間
// int Distance; // 距離
// int isTri = true, trigNow = 0, echoNow = 0;
int isDone = false;

// 最後角度區
int Y_Track_Up = 155, Y_Track_Down = 30, Y_Disc_Up = 155, Y_Disc_Down = 30;
int X_Track = 12, X_Disc = 104;
int Car_Servo_Up = 168, Car_Servo_Down = 100;
int Entrance_Servo_Down = 0, Entrance_Servo_Up = 135;

int angle_delayTime = 2000;

// ----------------------------------------------- 狀態設定 ^ ----------------------------------------------- //

void setup() {

    Serial.begin(9600); 

    for(int i = 0; i < 4; i++ ){
        pinMode(entrance_L298N_car[i], OUTPUT);
    }

    // 微動開關: INPUT
    pinMode(entranceButton, INPUT);
    pinMode(tailButton, INPUT);
    pinMode(discButton, INPUT);
    pinMode(camaraButton, INPUT);

    // pinMode(trigPin, OUTPUT);
    // pinMode(echoPin, INPUT);
    // digitalWrite(trigPin, LOW);

    pinMode(relay, OUTPUT);
    digitalWrite(relay, LOW);

    // 伺服馬達
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    car_servo.attach(car_servo_pin); 
    entrance_servo.attach(entrance_servo_pin);

    // 伺服馬達定位
    biaxial_servo_x.write(X_Track);
    biaxial_servo_y.write(Y_Track_Down);
    car_servo.write(Car_Servo_Up);
    entrance_servo.write(Entrance_Servo_Up);

    // 步進馬達
    disc_stepper.setSpeed(10);

    // 初始化 LCD
    lcd.init();
    lcd.backlight();

    setUpLCD(1, 0, "wait instruction");

    // 最後歸位
    delay(2000);
    biaxial_servo_x.detach();
    biaxial_servo_y.detach();
    car_servo.detach();
    entrance_servo.detach();
    Serial.println("----------- 等待指令中 -----------");
}

void loop() {

    
    if (Serial.available()) {
        
        String command = Serial.readStringUntil('\n'); // 收到的指令 // 讀取傳入的字串直到"\n"結尾

        // ---------------- 存放 START---------------- // 
        if (command == "GO_Storage") {
            digitalWrite(relay, HIGH); // 把繼電器打開

            // 開始步驟
            Serial.println("Input_The_Position_1");
            String get_position_1 =  Serial.readStringUntil('\n');
            int position_1 = get_position_1.toInt();
            Serial.println("輸入的位置 " + String(position_1));
            
            lcd.clear();  
            Serial.println("GO Storage");
            setUpLCD(1, 0, "GO Storage");
            setUpLCD(1, 2, "Y: Down, X: Track");  

            setUpLCD(1, 3, "Disc           " + String(position_1));  Serial.println("圓盤轉動位置至" + String(position_1));
            discRotate_withTimes(position_1); // TODO: 3為測試數值，之後接上資料庫做正確數值修改
            delay(1000);

            // 開始步驟 
            bool start = true; // true: start, false: stop

            // 開始動作 - 車子啟動
            Serial.println("微動開關 拍照");
            while(start == true){

                mfront(entrance_L298N_car); // 馬達前進
                setUpLCD(1, 1, "Running,  Front ");

                if (isDone == false &&  
                    checkTheBtnStatus(camaraButton, camaraButtonState, camaraButtonLastState, camaraButtonlastDebounceTime, globalDelayTime) == true
                ){
                    Serial.println("碰到攝像頭前面的按鈕");
                    start = false;
                    Serial.println("碰到 微動開關 停止運轉馬達");
                    mstop(entrance_L298N_car);mstop(entrance_L298N_car); // 馬達停下

                    // 等待5秒
                    unsigned long nowTempTime = millis();
                        // 拍照
                    Serial.println("Photograph, tempTime: " + String(nowTempTime) + ", millis():" + String(millis()) );

                    Serial.println("等待5秒");
                    while (millis() - nowTempTime <= 5000) {
                        setUpLCD(1, 3, + "Waiting ... " + String(5 - int(millis() - nowTempTime) / 1000) +  "  ");
                    }
                    setUpLCD(1, 3, "Not Distance Now");
                    Serial.println("重新啟動 正轉");

                    mfront(entrance_L298N_car);
                    isDone = true;
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
            time_for_car(500, 1, entrance_L298N_car);
            mstop(entrance_L298N_car); // 馬達停下
            setUpLCD(1, 1, "Stopping, Front ");

            delay(2000);

            // 機械手臂Y軸上升: 提取衣物(軌道)
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂Y軸上升: 提取衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 5, Y_Track_Down, Y_Track_Up);

            // 模型車掛臂收回
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("模型車掛臂收回");
            servo_with_time(car_servo, car_servo_pin, 10, Car_Servo_Up, Car_Servo_Down);

           // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Track, X_Disc - 15);
            delay(3500);
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Disc - 15, X_Disc);

            // 模型車掛臂露出
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("模型車掛臂露出");
            servo_with_time(car_servo, car_servo_pin, 10, Car_Servo_Down, Car_Servo_Up);

            // 反轉 ~ 停止(回到入口)
            setUpLCD(1, 1, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping,  Back");  Serial.println("反轉停止");

            // 機械手臂Y軸下降: 放下衣物(圓盤)
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂Y軸下降: 放下衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Disc_Up, Y_Disc_Down);

            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 5, X_Disc, X_Track);

            // 模型車掛臂露出
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("模型車掛臂露出");
            servo_with_time(car_servo, car_servo_pin, 10, Car_Servo_Down, Car_Servo_Up);

            // 結束步驟            
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            isDone = false;
            digitalWrite(relay, LOW); // 把繼電器打開
            Serial.println("Done");
        } 
        // ---------------- 存放 END ---------------- //

        // ---------------- 拿取 START---------------- //
        else if (command == "GO_PickUp_1") {
            digitalWrite(relay, HIGH); // 把繼電器打開

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
            setUpLCD(1, 3, "Disc           " + String(position_1));  Serial.println("圓盤轉動位置至" + String(position_1));
            discRotate_withTimes(position_1); // TODO: 3為測試數值，之後接上資料庫做正確數值修改
            delay(1000);

            // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 5, X_Track, X_Disc);

            // 機械手臂Y軸上升: 提取衣物(圓盤)  
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂Y軸上升: 提取衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Disc_Down, Y_Disc_Up);

            // 模型車掛臂收回
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("模型車掛臂收回");
            servo_with_time(car_servo, car_servo_pin, 10, Car_Servo_Up, Car_Servo_Down);

            // 正轉 ~ 停止(進入尾巴)
            setUpLCD(1, 1, "Running,  Front");  Serial.println("正轉至 碰到微動開關為止");
            motor_running(1, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping, Front");  Serial.println("正轉停止");

            // 持續兩秒 保證緊貼
            Serial.println("正轉持續兩秒 保證緊貼");
            time_for_car(500, 1, entrance_L298N_car);
            mstop(entrance_L298N_car); // 馬達停下
            setUpLCD(1, 1, "Stopping, Front ");

            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Disc, X_Track + 20);
            delay(2000);
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Track + 20, X_Track);
            delay(2000);

            // 模型車掛臂露出
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("模型車掛臂露出");
            servo_with_time(car_servo, car_servo_pin, 5, Car_Servo_Down, Car_Servo_Up);
            
            // 機械手臂Y軸下降: 放下衣物(軌道)
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂Y軸下降: 放下衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Track_Up, Y_Track_Down);

            // 反轉 ~ 停止(回到入口)
            setUpLCD(1, 1, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping,  Back");  Serial.println("反轉停止");

            delay(1000);

            // 入口停衣場 放下
//            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("入口停衣場 放下");
//            servo_with_time(entrance_servo, entrance_servo_pin, 1, Entrance_Servo_Up, Entrance_Servo_Down);

            // 結束動作
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            digitalWrite(relay, LOW); // 把繼電器關閉
            Serial.println("Done");
        }
        // ---------------- 拿取 END ---------------- //

        // ---------------- 拿取兩件第一次 START p2---------------- //
        else if (command == "GO_PickUp_2") {
            digitalWrite(relay, HIGH); // 把繼電器打開

            lcd.clear();

             // 入口停衣場 放下
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("入口停衣場 放下");
            servo_with_time(entrance_servo, entrance_servo_pin, 5, Entrance_Servo_Up, Entrance_Servo_Down);

            Serial.println("GO PickUp 1");
            setUpLCD(1, 0, "GO PickUp 1");   
            setUpLCD(1, 2, "Y: Down, X: Track");  

            // 開始步驟
            Serial.println("Input_The_Position_1");
            String get_position_1 =  Serial.readStringUntil('\n');
            int position_1 = get_position_1.toInt();
            Serial.println("輸入的位置 " + String(position_1));

            setUpLCD(1, 3, "Disc           " + String(position_1));  Serial.println("圓盤轉動位置至" + String(position_1));
            discRotate_withTimes(position_1); 
            delay(1000);

            // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 5, X_Track, X_Disc);

            // 機械手臂Y軸上升: 提取衣物(圓盤)  
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂Y軸上升: 提取衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Disc_Down, Y_Disc_Up);

            // 模型車掛臂收回
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("模型車掛臂收回");
            servo_with_time(car_servo, car_servo_pin, 10, Car_Servo_Up, Car_Servo_Down);

            // 正轉 ~ 停止(進入尾巴)
            setUpLCD(1, 1, "Running,  Front");  Serial.println("正轉至 碰到微動開關為止");
            motor_running(1, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping, Front");  Serial.println("正轉停止");

            // 持續兩秒 保證緊貼
            Serial.println("正轉持續兩秒 保證緊貼");
            time_for_car(500, 1, entrance_L298N_car);
            mstop(entrance_L298N_car); // 馬達停下
            setUpLCD(1, 1, "Stopping, Front ");

            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Disc, X_Track + 20);
            delay(2000);
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Track + 20, X_Track);
            delay(2000);

            // 模型車掛臂露出
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("模型車掛臂露出");
            servo_with_time(car_servo, car_servo_pin, 5, Car_Servo_Down, Car_Servo_Up);
            
            // 機械手臂Y軸下降: 放下衣物(軌道)
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂Y軸下降: 放下衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Track_Up, Y_Track_Down);

            // 反轉 ~ 停止(回到入口)
            setUpLCD(1, 1, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping,  Back");  Serial.println("反轉停止");

            // 入口停衣場 抬起
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("入口停衣場 抬起");
            servo_with_time(entrance_servo, entrance_servo_pin, 5, Entrance_Servo_Down, Entrance_Servo_Up);

            // 結束動作
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            digitalWrite(relay, LOW); // 把繼電器關閉
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
            
            // 結束動作
            Serial.println("Done");
        }
        // ---------------- 直線到底(出來) END ---------------- //

        
        else if (command == "GO_Disc"){

            Serial.println("GO_Disc");
            lcd.clear();
            setUpLCD(1, 0, "disc around now");

            // 開始旋轉
            digitalWrite(relay, HIGH); // 把繼電器打開
            discRotate_withTimes(1); // TODO: 3為測試數值，之後接上資料庫做正確數值修改


            // 結束
            delay(3000);
            digitalWrite(relay, HIGH); // 把繼電器打開

            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            Serial.println("Done");
        }

        // ---------------- 推進去拍照 START---------------- // 
        else if (command == "GO_TakeAPhoto_S1") {
            digitalWrite(relay, HIGH); // 把繼電器打開
            
            lcd.clear();  
            Serial.println("GO_TakeAPhoto_S1");
            setUpLCD(1, 0, "GO_TakeAPhoto_S1");
            setUpLCD(1, 2, "Y: Down, X: Track");  

            // 開始步驟 
            bool start = true; // true: start, false: stop

            // 開始動作 - 車子啟動
            Serial.println("等待超音波或微動開關");
            while(start == true){

                mfront(entrance_L298N_car); // 馬達前進
                setUpLCD(1, 1, "Running,  Front ");

                // 是否到底(停下)
                if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
                ||  checkTheBtnStatus( tailButton, tailButtonState, tailButtonLastState, tailButtonlastDebounceTime, globalDelayTime) == true
                ||  checkTheBtnStatus( camaraButton, camaraButtonState, camaraButtonLastState, camaraButtonlastDebounceTime, globalDelayTime) == true
                ){
                    mstop(entrance_L298N_car);mstop(entrance_L298N_car); // 馬達停下
                    Serial.println("GO Storage Button True");
                    start = false;
                    Serial.println("碰到 微動開關 停止運轉馬達");
                    // 等待5秒
                    unsigned long nowTempTime = millis();
                    // 拍照
                    Serial.println("Photograph, tempTime: " + String(nowTempTime) + ", millis():" + String(millis()) );

                    Serial.println("等待5秒");
                    while (millis() - nowTempTime <= 5000) {
                        setUpLCD(1, 3, + "Waiting ... " + String(5 - int(millis() - nowTempTime) / 1000) +  "  ");
                    }
                    setUpLCD(1, 3, "Not Distance Now");
                    
                    isDone = true;
                    start = false;
                }

            }
//            mstop(entrance_L298N_car);mstop(entrance_L298N_car); // 馬達停下
            
            // 結束步驟            
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            isDone = false;
            digitalWrite(relay, LOW); // 把繼電器打開
            Serial.println("Done");
        } 
        // ---------------- 進去拍照 END ---------------- //

        // ---------------- 拍照後存放 START---------------- // 
        else if (command == "GO_Storage_S2") {
            digitalWrite(relay, HIGH); // 把繼電器打開
            
            lcd.clear();  
            Serial.println("GO_Storage_S2");
            setUpLCD(1, 0, "GO_Storage_S2");
            setUpLCD(1, 2, "Y: Down, X: Track");

            // 開始步驟
            Serial.println("Input_The_Position_1");
            String get_position_1 =  Serial.readStringUntil('\n');
            int position_1 = get_position_1.toInt();
            Serial.println("輸入的位置 " + String(position_1));

            setUpLCD(1, 3, "Disc           " + String(position_1));  Serial.println("圓盤轉動位置至" + String(position_1));
            discRotate_withTimes(position_1); // TODO: 3為測試數值，之後接上資料庫做正確數值修改
            delay(1000);

            // 正轉
            setUpLCD(1, 1, "Running,  Front");  Serial.println("正轉至 碰到微動開關為止");
            motor_running(1, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping,  Front");  Serial.println("正轉停止");

            // 持續兩秒 保證緊貼
            Serial.println("正轉持續兩秒 保證緊貼");
            time_for_car(500, 1, entrance_L298N_car);
            mstop(entrance_L298N_car); // 馬達停下
            setUpLCD(1, 1, "Stopping, Front ");

            delay(2000);

            // 機械手臂Y軸上升: 提取衣物(軌道)
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂Y軸上升: 提取衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Track_Down, Y_Track_Up);

            // 模型車掛臂收回
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("模型車掛臂收回");
            servo_with_time(car_servo, car_servo_pin, 10, Car_Servo_Up, Car_Servo_Down);

             // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Track, X_Disc - 20);
            delay(2000);
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Disc - 20, X_Disc);

            // 機械手臂Y軸下降: 放下衣物(圓盤)
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂Y軸下降: 放下衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Disc_Up, Y_Disc_Down);

             // 模型車掛臂露出
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("模型車掛臂露出");
            servo_with_time(car_servo, car_servo_pin, 5, Car_Servo_Down, Car_Servo_Up);

            // 反轉 ~ 停止(回到入口)
            setUpLCD(1, 1, "Running,  Back ");  Serial.println("反轉至 碰到微動開關為止");
            motor_running(2, entrance_L298N_car);
            setUpLCD(1, 1, "Stopping,  Back");  Serial.println("反轉停止");

            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 5, X_Disc, X_Track);

            // 結束步驟            
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            isDone = false;
            digitalWrite(relay, LOW); // 把繼電器打開
            Serial.println("Done");
        } 
        // ---------------- 進去拍照 END ---------------- //

        // ---------------- 測試存放位置 START---------------- // 
        else if (command == "test_put") {
            digitalWrite(relay, HIGH);
          
            lcd.clear();
            Serial.println("test_put");
            setUpLCD(1, 0, "test_put");

            // 機械手臂Y軸上升: 提取衣物(軌道)
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂Y軸上升: 提取衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Track_Down, Y_Track_Up);

            delay(1000);
            discRotate_withTimes(1);
            
            // 結束
            delay(2000);

            // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Track, X_Disc - 20);
            delay(1000);
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Disc - 20, X_Disc);
            

            // 機械手臂Y軸下降: 放下衣物(圓盤)
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂Y軸下降: 放下衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Disc_Up, Y_Disc_Down);

            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 5, X_Disc, X_Track);

            // 結束步驟            
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            isDone = false;
            digitalWrite(relay, LOW);

            Serial.println("Done");
        } 

        else if (command == "test_get"){
            digitalWrite(relay, HIGH);
          
            lcd.clear();
            Serial.println("test_get");
            setUpLCD(1, 0, "test_get");

            // TODO: 圓盤轉至「位置指定」
            setUpLCD(1, 3, "Disc           " + String(1));  Serial.println("圓盤轉動位置至" + String(1));
            discRotate_withTimes(1); // TODO: 3為測試數值，之後接上資料庫做正確數值修改
            delay(1000);
            
            // 機械手臂X軸: 轉至圓盤
            setUpLCD(1, 2, "Y: Down, X: Disc ");  Serial.println("機械手臂X軸: 轉至圓盤");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 5, X_Track, X_Disc);
            
            // 機械手臂Y軸上升: 提取衣物(圓盤)  
            setUpLCD(1, 2, "Y: Up  , X: Disc ");  Serial.println("機械手臂Y軸上升: 提取衣物(圓盤)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Disc_Down, Y_Disc_Up);
            
            // 機械手臂X軸: 轉至軌道
            setUpLCD(1, 2, "Y: Up  , X: Track");  Serial.println("機械手臂X軸: 轉至軌道");
            servo_with_time(biaxial_servo_x, biaxial_servo_x_pin, 1, X_Disc, X_Track);
            delay(2000);
            
            // 機械手臂Y軸下降: 放下衣物(軌道)
            setUpLCD(1, 2, "Y: Down, X: Track");  Serial.println("機械手臂Y軸下降: 放下衣物(軌道)");
            servo_with_time(biaxial_servo_y, biaxial_servo_y_pin, 1, Y_Track_Up, Y_Track_Down);
            
            // 結束動作
            lcd.clear();
            setUpLCD(1, 0, "wait instruction");
            digitalWrite(relay, LOW); // 把繼電器關閉
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

void time_for_car(int timesecond, int type, int l298n_car[4]){
    bool temp_start = true;  // true: start, false: stop
    long temp_time = millis();
    while(millis() - temp_time <= timesecond){

        if(type == 1 ){
            mfront(l298n_car); // 馬達前進
        }
        else if (type == 2){
            mback(l298n_car); // 馬達後退
        }
    }
    mstop(l298n_car);
}

// type = 1: 前進, type = 2: 後退
void motor_running(int type, int l298n_car[4]){
    bool temp_start = true;  // true: start, false: stop
    long temp_time = millis();
    while(temp_start == true){

        if(type == 1 ){
            mfront(l298n_car); // 馬達前進
        }
        else if (type == 2){
            mback(l298n_car); // 馬達後退
        }

        if(millis() - temp_time > 1000){
          // 是否到底(停下)
            if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
            ||  checkTheBtnStatus( tailButton, tailButtonState, tailButtonLastState, tailButtonlastDebounceTime, globalDelayTime) == true
            ){
                Serial.println("GO Storage Button True");
                temp_start = false;
            }
        }
    }
    mstop(l298n_car);
} 


void discRotate_withTimes(int times){

    Serial.println("discRotate_withTimes have to rotate " + String(times) + " Times");
    long temp_time = millis();
    int now_times = 0;
    // 開始旋轉 
    
    bool disc_start = true;  // true: start, false: stop
    //disc_start == true | now_times <= times
    while( now_times != times){

        disc_stepper.step(-1);  // 20/200 = 1/10
        if(millis() - temp_time > 500){
          if( checkTheBtnStatus(discButton, discButtonState, discButtonLastState, discButtonlastDebounceTime, globalDelayTime) == true){
//              disc_start = false;
              now_times++;
          }
        }
       
    }
    // 微動開關按了才結束
    Serial.println("轉了" + String(now_times) + "次");
}

void servo_with_time(Servo servo_now, int servo_pin, int speed_now, int angle_now, int angle_need){
    servo_now.attach(servo_pin);

    if ( angle_now < angle_need){
        for( int i = angle_now; i <= angle_need; i += speed_now ){
            servo_now.write(i);
            delay(15);
    }
    }else{
        for( int i = angle_now; i >= angle_need; i -= speed_now ){
            servo_now.write(i);
            delay(15);
        }
    }

    delay(1000);
    
    // 結束連線
    delay(angle_delayTime);
    servo_now.detach();
}
