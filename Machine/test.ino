#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Wire.h>

// LCD 
LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、2為LCD顯示器大小。


// ----------------------------------------------- 變數設定 ----------------------------------------------- //
long globalDelayTime = 50;  // 消斗的時間

const int entranceButton = 22; // 入口的微動開關
int entranceButtonState;
int entranceButtonLastState = LOW;
long entranceButtonlastDebounceTime = 0;  // 按了最後一次被觸發

const int exportButton = 23; // 出口的微動開關
int exportButtonState;
int exportButtonLastState = LOW;
long exportButtonlastDebounceTime = 0;  // 按了最後一次被觸發

// 開始的微動開關
const int startButton = 31;  // 切換開始
int startButtonState;
int startButtonLastState = LOW;
long startButtonlastDebounceTime = 0;  // 按了最後一次被觸發

// 車車(減速馬達)的L298N
const int entrance_L298N1_In1 = 2;
const int entrance_L298N1_In2 = 3;
const int export_L298N1_In3 = 4;
const int export_L298N1_In4 = 5;

// 超音波
const int trigPin = 13;
const int echoPin = 12;
int Duration;
int Distance;
int isTri = true, trigNow = 0, echoNow = 0, isDone = false;

// 全域控制
int nowStep = 2;     // 1: 前進, 2: 後退
bool start = false;  // true: start, false: stop

// ----------------------------------------------- 變數設定 ----------------------------------------------- //

void setup() {

    Serial.begin(9600); 

    pinMode(entrance_L298N1_In1, OUTPUT);
    pinMode(entrance_L298N1_In2, OUTPUT);
    pinMode(export_L298N1_In3, OUTPUT);
    pinMode(export_L298N1_In4, OUTPUT);

    pinMode(entranceButton, INPUT);
    pinMode(exportButton, INPUT);
    pinMode(startButton, INPUT);

    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    digitalWrite(trigPin, LOW);

    // 初始化 LCD
    lcd.init();
    lcd.backlight();
}

void loop() {

    //Serial.println("now start: " + String(start) + ", step:" + String(nowStep));    
    
    if (Serial.available()) {

        String command = Serial.readStringUntil('\n'); // 收到的指令 // 讀取傳入的字串直到"\n"結尾

        // ---------------- 存放 START---------------- //
        if (command == "GO_Storage" && nowStep == 2 && start == false) {
            Serial.println("GO Storage");

            // 開始步驟   
            nowStep = 1;
            start = true;
            setUpLCD(1, 0, "start:" + String((start == true) ? "true " : "false"));
            setUpLCD(1, 1, "nowStep:" + String((nowStep == 1) ? "front" : "back " ));
            

            // 動作
            digitalWrite(LED_BUILTIN, HIGH);
            while(start == true){
                // mfront(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4); // 馬達前進
                
                // 準備拍照
                if (isTri == true && isDone == false) { // 可發射 且 未完成拍照 (持續發射)
                    digitalWrite(trigPin, HIGH);    // 發射超音波
                    isTri = false;                  // 不可發射
                    trigNow = millis();             // 計算發射時間(start)
                } else if (isTri == false && millis() - trigNow >= 500) { // 不可發射 且 發射時間大於0.5s (停止發射)
                    isTri = true;                           // 可重新發射了

                    digitalWrite(trigPin, LOW);             // 停止發射超音波
                    Duration = pulseIn(echoPin, HIGH);      // 超音波發射到接收的時間
                    Distance = Duration * 0.034 / 2;        // 計算距離(cm)

                    setUpLCD(1, 2, "Distance " + String(Distance) + "    ");

                    if (Distance <= 20) {                   // 距離小於 20cm
                        // 稍微停止一下
                        // mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);

                        // 拍照
                        Serial.println("Photograph");

                        // 等待5秒
                        int nowTempTime = millis();
                        while (millis() - nowTempTime <= 5000) {
                            setUpLCD(1, 2, "Waiting ... " + String(5 - int(millis() - nowTempTime) / 1000) +  "  ");
                        }
                        setUpLCD(1, 2, "Not Distance Now ");
                        // mfront(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
                        isDone = true;
                    }
                }
                
                // 是否到底(停下)
                if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
//              ||  checkTheBtnStatus(exportButton, exportButtonState, exportButtonLastState, exportButtonlastDebounceTime, globalDelayTime) == true
                ){
                    Serial.println("GO Storage Button True");
                    start = false;
                }
            }
            // mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4); // 馬達停下

            // 結束步驟
            setUpLCD(1, 0, "start:" + String((start == true) ? "true " : "false"));
            setUpLCD(1, 1, "nowStep:" + String((nowStep == 1) ? "front" : "back " ));
            digitalWrite(LED_BUILTIN, LOW);
            Serial.println("Done");

        } 
        // ---------------- 存放 END ---------------- //

        // ---------------- 拿取 START---------------- //
        else if (command == "GO_PickUp" && nowStep == 1 && start == false) {
            Serial.println("GO PickUp");

            // 開始步驟   
            nowStep = 2;
            start = true;
            setUpLCD(1, 0, "start:" + String((start == true) ? "true " : "false"));
            setUpLCD(1, 1, "nowStep:" + String((nowStep == 1) ? "front" : "back " ));

            // 動作
            digitalWrite(LED_BUILTIN, HIGH);
            while(start == true){
//              mback(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
                if( checkTheBtnStatus(entranceButton, entranceButtonState, entranceButtonLastState, entranceButtonlastDebounceTime, globalDelayTime) == true
                // ||  checkTheBtnStatus(exportButton, exportButtonState, exportButtonLastState, exportButtonlastDebounceTime, globalDelayTime) == true
                ){
                    Serial.println("GO PickUp Button True");
                    start = false;
                }
            }
            // mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4); // 馬達停下

            // 結束步驟
            setUpLCD(1, 0, "start:" + String((start == true) ? "true " : "false"));
            setUpLCD(1, 1, "nowStep:" + String((nowStep == 1) ? "front" : "back " ));
            digitalWrite(LED_BUILTIN, LOW);

            Serial.println("Done");
        }
        // ---------------- 拿取 END ---------------- //

        // ---------------- 直線到底(前進) START---------------- //
        else if (command == "GO_Straight_Front") {
            Serial.println("GO Straight Front");
        }
        // ---------------- 直線到底(前進) END ---------------- //

        // ---------------- 直線到底(出來) START---------------- //
        else if (command == "GO_Straight_Back") {
            Serial.println("GO Straight Back");
        }
        // ---------------- 直線到底(出來) END ---------------- //

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
    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    digitalWrite(In3, HIGH);
    digitalWrite(In4, LOW);
}
// 步進馬達: 後退
void mback(int In1, int In2, int In3, int In4) {
    digitalWrite(In1, LOW);
    digitalWrite(In2, HIGH);
    digitalWrite(In3, LOW);
    digitalWrite(In4, HIGH);
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