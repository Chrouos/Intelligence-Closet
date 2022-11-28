#include <Stepper.h>
// 定義步進馬達轉一圈所需的步數及輸出的腳位
Stepper stepper(200,
                2,
                3,
                4,
                5);  // 360 / 120(120步可以轉一圈) = 30(每一步30度)
const int startButton = 22;  // 切換開始
int startButtonState;
int startButtonLastState = LOW;
long startButtonlastDebounceTime = 0;  // 按键最后一次被触发
long startButtondebounceDelay =
    50;  // 为了滤去抖动暂停的时间，如果发现输出不正常增加这个值

void setup() {
    // 將馬達速度設定為每分鐘80轉(RPM)
    stepper.setSpeed(52);
    Serial.begin(9600); 

    Serial.println("start");
    digitalWrite(48, HIGH);

}
void loop() {
  
    // -------------------- start button -------------------- //
    int startButtonnRead = digitalRead(startButton);
    if (startButtonnRead != startButtonLastState) {  // 如果按键状态和上次不同
        startButtonlastDebounceTime = millis();  // 记录初始时间
    }
    if ((millis() - startButtonlastDebounceTime) > startButtondebounceDelay) {
        if (startButtonnRead != startButtonState) {  // 如果按键状态改变了
            startButtonState = startButtonnRead;
             Serial.println("press");
            // 切換了開始
            if (startButtonnRead == HIGH) {
                stepper.step(200 / 100);  //正半圈
                Serial.println("1 ");
            }
        }
    }
    startButtonLastState = startButtonnRead;  // 保存处理结果
                                              // 馬達行進步數
}
    