#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Wire.h>

// LCD 
LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、2為LCD顯示器大小。


// ----------------------------------------------- 變數設定 ----------------------------------------------- //

const int entranceButton = 22; // 內部的微動開關
int entranceButtonState;
int entranceButtonLastState = LOW;
long entranceButtonlastDebounceTime = 0;  // 按了最後一次被觸發
long entranceButtondebounceDelay =  50;  // 消斗的時間

const int exportButton = 24; // 外部的微動開關
int exportButtonState;
int exportButtonLastState = LOW;
long exportButtonlastDebounceTime = 0;  // 按了最後一次被觸發
long exportButtondebounceDelay = 50;  // 消斗的時間

// 開始的微動開關
const int startButton = 23;  // 切換開始
int startButtonState;
int startButtonLastState = LOW;
long startButtonlastDebounceTime = 0;  // 按了最後一次被觸發
long startButtondebounceDelay = 50;  // 消斗的時間

// 車車(減速馬達)的L298N
const int entrance_L298N1_In1 = 6;
const int entrance_L298N1_In2 = 7;
const int export_L298N1_In3 = 8;
const int export_L298N1_In4 = 9;

// 超音波
const int trigPin = 40;
const int echoPin = 42;
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

    lcd.setCursor(1, 0);  // (colum, row) 從第一排的第三個位置開始顯示
    lcd.print("start:" + String((start == 1) ? "true " : "false"));
    lcd.setCursor(1, 1);  // (colum, row) 從第一排的第三個位置開始顯示
    lcd.print("nowStep:" + String(nowStep));

    // -------------------- start button -------------------- //
    int startButtonnRead = digitalRead(startButton);
    if (startButtonnRead != startButtonLastState) {  // 如果按键状态和上次不同
        startButtonlastDebounceTime = millis();  // 记录初始时间
    }
    if ((millis() - startButtonlastDebounceTime) > startButtondebounceDelay) {
        if (startButtonnRead != startButtonState) {  // 如果按键状态改变了
            startButtonState = startButtonnRead;

            // 切換了開始
            if (startButtonnRead == HIGH) {
                nowStep = (nowStep == 2) ? 1 : 2;
                start = true;

                Serial.println("now start: " + String(nowStep));
            }
        }
    }
    startButtonLastState = startButtonnRead;  // 保存处理结果
    // -------------------- start button -------------------- //

    if (nowStep == 1 && start == true) {
        digitalWrite(LED_BUILTIN, HIGH);
        mfront(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
    } else if (nowStep == 2 && start == true) {
        digitalWrite(LED_BUILTIN, HIGH);
        mback(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
    } else {
        mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
    }

    // -------------------- entrance or export button -------------------- //
    int entranceButtonRead = digitalRead(entranceButton);
    if (entranceButtonRead !=
        entranceButtonLastState) {  // 如果按键状态和上次不同
        entranceButtonlastDebounceTime = millis();  // 记录初始时间
    }

    if ((millis() - entranceButtonlastDebounceTime) >
        entranceButtondebounceDelay) {
        if (entranceButtonRead != entranceButtonState) {  // 如果按键状态改变了
            entranceButtonState = entranceButtonRead;

            // 切換了開始
            if (entranceButtonRead == HIGH) {
                mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
                start = false;
            }
        }
    }
    entranceButtonLastState = entranceButtonRead;  // 保存处理结果

    int exportButtonRead = digitalRead(exportButton);
    if (exportButtonRead != exportButtonLastState) {  // 如果按键状态和上次不同
        exportButtonlastDebounceTime = millis();  // 记录初始时间
    }
    if ((millis() - exportButtonlastDebounceTime) > exportButtondebounceDelay) {
        if (exportButtonRead != exportButtonState) {  // 如果按键状态改变了
            exportButtonState = exportButtonRead;

            // 切換了開始
            if (exportButtonRead == HIGH) {
                mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
                start = false;
            }
        }
    }
    exportButtonLastState = exportButtonRead;  // 保存处理结果
    // -------------------- entrance button -------------------- //
    Serial.println("nowStep " + String(nowStep) + ", start " + String(start));

    if (nowStep == 1 && start == true) {
        if (isTri == true && isDone == false) {
            digitalWrite(trigPin, HIGH);  //發射超音波
            isTri = false;
            trigNow = millis();
        } else if (isTri == false && millis() - trigNow >= 500) {
            digitalWrite(trigPin, LOW);
            Duration = pulseIn(echoPin, HIGH);  //超音波發射到接收的時間
            Distance = Duration * 0.034 / 2;  //計算距離(cm)
            isTri = true;
            Serial.println("Distance " + String(Distance));
            lcd.setCursor(1, 2);  // (colum, row)從第一排的第三個位置開始顯示
            lcd.print("Distance " + String(Distance) + "    ");

            if (Distance <= 20) {
                mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
                int nowTempTime = millis();
                while (millis() - nowTempTime <= 5000) {
                    lcd.setCursor(
                        1, 2);  // (colum, row)從第一排的第三個位置開始顯示
                    lcd.print("Waiting ... " + String(5 - int(millis() - nowTempTime) / 1000) +  "  ");
                }
                lcd.setCursor(1,
                              2);  // (colum, row)從第一排的第三個位置開始顯示
                lcd.print("Not Distance Now ");
                mfront(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3, export_L298N1_In4);
                isDone = true;
            }
        }
    } else if (nowStep == 2) {
        isDone = false;
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