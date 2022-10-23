#include <Servo.h>

// 入口的微動開關
const int entranceButton = 22;
int entranceButtonState;
int entranceButtonLastState = LOW;
long entranceButtonlastDebounceTime = 0;  // 按键最后一次被触发
long entranceButtondebounceDelay =
    50;  // 为了滤去抖动暂停的时间，如果发现输出不正常增加这个值

// 出口的微動開關
const int exportButton = 23;
int exportButtonState;
int exportButtonLastState = LOW;
long exportButtonlastDebounceTime = 0;  // 按键最后一次被触发
long exportButtondebounceDelay =
    50;  // 为了滤去抖动暂停的时间，如果发现输出不正常增加这个值

// 開始的微動開關
const int startButton = 31;  // 切換開始
int startButtonState;
int startButtonLastState = LOW;
long startButtonlastDebounceTime = 0;  // 按键最后一次被触发
long startButtondebounceDelay =
    50;  // 为了滤去抖动暂停的时间，如果发现输出不正常增加这个值

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
}

int nowStep = 2;     // 1: 前進, 2: 後退
bool start = false;  // true: start, false: stop
void loop() {
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
        mfront(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3,
               export_L298N1_In4);
    } else if (nowStep == 2 && start == true) {
        digitalWrite(LED_BUILTIN, HIGH);
        mback(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3,
              export_L298N1_In4);
    } else {
        mstop(entrance_L298N1_In1, entrance_L298N1_In2, export_L298N1_In3,
              export_L298N1_In4);
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
                mstop(entrance_L298N1_In1, entrance_L298N1_In2,
                      export_L298N1_In3, export_L298N1_In4);
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
                mstop(entrance_L298N1_In1, entrance_L298N1_In2,
                      export_L298N1_In3, export_L298N1_In4);
                start = false;
            }
        }
    }
    exportButtonLastState = exportButtonRead;  // 保存处理结果
    // -------------------- entrance button -------------------- //

    if (nowStep == 1) {
        if (isTri == true) {
            digitalWrite(trigPin, HIGH);  //發射超音波
            isTri = false;
            trigNow = millis();
        } else if (isTri == false && millis() - trigNow >= 1000) {
            digitalWrite(trigPin, LOW);
            Duration = pulseIn(echoPin, HIGH);  //超音波發射到接收的時間
            Distance = Duration * 0.034 / 2;  //計算距離(cm)
            isTri = true;

            if (Distance <= 20 && isDone == false) {
                mstop(entrance_L298N1_In1, entrance_L298N1_In2,
                      export_L298N1_In3, export_L298N1_In4);
                delay(2000);
                mfront(entrance_L298N1_In1, entrance_L298N1_In2,
                       export_L298N1_In3, export_L298N1_In4);
                isDone = true;
            }
        }
    } else if (nowStep == 2) {
        isDone = false;
    }
}

void mstop(int In1, int In2, int In3, int In4) {
    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
}
void mfront(int In1, int In2, int In3, int In4) {
    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    digitalWrite(In3, HIGH);
    digitalWrite(In4, LOW);
}
void mback(int In1, int In2, int In3, int In4) {
    digitalWrite(In1, LOW);
    digitalWrite(In2, HIGH);
    digitalWrite(In3, LOW);
    digitalWrite(In4, HIGH);
}
