#include <Servo.h>
#include <Stepper.h>

// ----------------------- 腳位 v ----------------------- //
const int biaxial_servo_x_pin = A2;     // 伺服馬達 (X)
const int biaxial_servo_y_pin = A3;     // 伺服馬達 (Y)
Stepper stepperX(200, 8, 9, 10, 11);    // 步進馬達 (X)
Stepper stepperY(200, 2, 3, 4, 5);      // 步進馬達 (Y)
const int x_StopButton = 23;            // 歸零按鈕 (X)
const int y_StopButton = 22;            // 歸零按鈕 (Y)

// ----------------------- 定義 v ----------------------- //
Servo biaxial_servo_x, biaxial_servo_y; // 雙軸伺服馬達
const int stepperSpeed = 80;

// ----------------------- 參數 v ----------------------- //
int servo_x_pos = 80, servo_y_pos = 50; // 手臂位置預設

int angle = 1, angle_delayTime = 15;    // 手臂必要參數
long globalDelayTime = 50;              // 按鈕消斗的時間
int x_StopButtonState;                  // (歸零按鈕 X) 微動開關的狀態
int x_StopButtonLastState = LOW;        // (歸零按鈕 X) 微動開關的最後狀態
long x_StopButtonlastDebounceTime = 0;  // (歸零按鈕 X) 按了最後一次被觸發
int y_StopButtonState;                  // (歸零按鈕 Y)微動開關的狀態
int y_StopButtonLastState = LOW;        // (歸零按鈕 Y)微動開關的最後狀態
long y_StopButtonlastDebounceTime = 0;  // (歸零按鈕 Y) 按了最後一次被觸發


void setup() {

    Serial.begin(9600);

    // 按鈕設定
    pinMode(x_StopButton, INPUT);
    pinMode(y_StopButton, INPUT);

    // 伺服馬達
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    biaxial_servo_y.write(servo_y_pos);
    biaxial_servo_x.attach(biaxial_servo_x_pin);

    // 步進馬達，將馬達速度設定為每分鐘 stepperSpeed 轉(RPM)
    stepperX.setSpeed(stepperSpeed);
    stepperY.setSpeed(stepperSpeed);
    
    delay(1000);

    Serial.println("----------- 等待指令中 -----------");
}


void loop(){

    if (Serial.available()) {
        
        String command = Serial.readStringUntil('\n'); // 收到的指令 // 讀取傳入的字串直到"\n"結尾
        
        // -------------------------------------------------------- 放衣服
        if (command == "Put_The_Clothes") {

            // 從外部輸入「空位置」
            Serial.println("please_input_str_position");
            String str_position =  Serial.readStringUntil('\n');
            int _position = str_position.toInt();
            Serial.println("目前可放置的位置 " + String(_position));
            
            // 從入口到放下衣物，再到歸零位置
            put_entrance_position_zero(_position);

            // 結束指令
            Serial.println("Done"); 
        }

        // -------------------------------------------------------- 拿衣服
        else if (command == "Take_The_Clothes"){

            // 從外部輸入「空位置」
            Serial.println("please_input_str_position");
            String str_position =  Serial.readStringUntil('\n');
            int _position = str_position.toInt();
            Serial.println("目前可放置的位置 " + String(_position));

            take_zero_position_entrance(_position); // 將衣服從位置放到入口

            // 結束指令
            Serial.println("Done"); 
        }

        else if (command == "Put_Entrance_Position_Zero"){

            // 從外部輸入「空位置」
            Serial.println("please_input_str_position");
            String str_position =  Serial.readStringUntil('\n');
            int _position = str_position.toInt();
            Serial.println("目前可放置的位置 " + String(_position));

            put_entrance_position_zero(_position);

            // 結束指令
            Serial.println("Done"); 
        }

        else if (command == "Put_Zero_Position_Zero"){

            // 從外部輸入「空位置」
            Serial.println("please_input_str_position");
            String str_position =  Serial.readStringUntil('\n');
            int _position = str_position.toInt();
            Serial.println("目前可放置的位置 " + String(_position));

            // 歸零 -> 位置 -> 歸零
            put_zero_position_zero(_position);

            // 結束指令
            Serial.println("Done"); 
        }

        // -------------------------------------------------------- 從歸零位到入口
        else if (command == "Zero_To_Entrance"){
            
            zero_to_entrance();

            // 結束指令
            Serial.println("Done"); 
        }
        
        // -------------------------------------------------------- 從入口到歸零位
        else if (command == "Entrance_To_Zero"){
            
            entrance_to_zero();

            // 結束指令
            Serial.println("Done"); 
        }

        // -------------------------------------------------------- 天車歸位
        else if (command == "Return_Crane_Zero"){
            
            correction_zero();

            // 結束指令
            Serial.println("Done"); 
        }

        else if (command == "TEST"){
//          correction_zero();

            // 結束指令
            Serial.println("Done"); 
        }

        else{
            // 結束指令
            Serial.println("Done"); 
        }

        delay(1000);

    }

}


// ----------------------- 預設函數 v ----------------------- //

// 手臂左轉
void arm_left() {   
    Serial.println("手臂向左");
    while (servo_x_pos + (-1 * angle) >= 0) {
        servo_x_pos += (-1 * angle);
        biaxial_servo_x.attach(biaxial_servo_x_pin);
        biaxial_servo_x.write(servo_x_pos);
        delay(angle_delayTime * 2);
    }
}

// 手臂右轉
void arm_right() {  
    Serial.println("手臂向右");
    while (servo_x_pos + (1 * angle) <= 92) {
        servo_x_pos += (1 * angle);
        biaxial_servo_x.attach(biaxial_servo_x_pin);
        biaxial_servo_x.write(servo_x_pos);
        delay(angle_delayTime);
    }
}

// 手臂放下
void arm_down() {   
    Serial.println("手臂向下");
    while (servo_y_pos + (1 * angle) <= 62) {
        servo_y_pos += (1 * angle);
        biaxial_servo_y.attach(biaxial_servo_y_pin);
        biaxial_servo_y.write(servo_y_pos);
        delay(angle_delayTime * 2);
    }
}

// 手臂勾起
void arm_up() {    
    Serial.println("手臂向上");
    while (servo_y_pos + (-1 * angle) >= 36) {
        servo_y_pos += (-1 * angle);
        biaxial_servo_y.attach(biaxial_servo_y_pin);
        biaxial_servo_y.write(servo_y_pos);
        delay(angle_delayTime * 2);
    }
}

// 確認按鈕狀況
int checkTheBtnStatus(const int button, int& buttonState, int& buttonLastState, long& buttonlastDebounceTime, long delayTime){
    int buttonRead = digitalRead(button);
    if (buttonRead != buttonLastState) {  // 如果案件狀態和上次不同
        buttonlastDebounceTime = millis();  // 記錄初始時間
    }

    if ((millis() - buttonlastDebounceTime) > delayTime) {
        if (buttonRead != buttonState) {  // 如果案件狀態改變
            buttonState = buttonRead;

            // 切換了開始
            if (buttonRead == HIGH) {
                return true;
            }
        }
    }
    buttonLastState = buttonRead;  // 保存處理狀況
    return false;
}

// 天車 X, Y 軸歸零
void correction_zero(){
    int run_return_x = -25, run_return_y = -25;

    // (1) 先將 y 拖回來，碰到微動開關後停止
    while (run_return_y != 0){
        // 是否到底(停下) Y
        if( checkTheBtnStatus( y_StopButton, y_StopButtonState, y_StopButtonLastState, y_StopButtonlastDebounceTime, globalDelayTime) == true
        ){
            run_return_y = 0;
            Serial.println("碰到微動開關 Y 停止");
        }
        stepperY.step(run_return_y);
    }

    // (2) 再將 x 拖回來，碰到微動開關後停止
    while ( run_return_x != 0){

        // 是否到底(停下) X
        if( checkTheBtnStatus( x_StopButton, x_StopButtonState, x_StopButtonLastState, x_StopButtonlastDebounceTime, globalDelayTime) == true
        ){
        run_return_x = 0;
        Serial.println("碰到微動開關 X 停止");
        }
    
        stepperX.step(run_return_x);
    }
}


void take_zero_position_entrance(int pos){

    // 預設天車位置
    int x = 300 + ((pos - 1) * 500);
    int y = 2150;

    // 放下
    arm_down();
    delay(1000);

    // 開始移動
    stepperX.step(x);
    stepperY.step(y);

    // 拿取
    arm_up();
    delay(1000);

    // 到入口
    stepperY.step(y * -1);
    stepperX.step(4300 - x);
    
}

void put_entrance_position_zero(int pos){

    // 預設天車位置
    int x = 300 + ((pos - 1) * 500);
    int y = 2150;

    // 拿取
    arm_up();
    delay(1000);

    // 開始移動
    stepperX.step(x - 4300);
    stepperY.step(y);
    delay(1000); // 到定位

    // 放下
    arm_down();
    delay(1000);
    
    // 歸位
    stepperY.step(y * -1);
    stepperX.step(x * -1);

}

void entrance_to_zero(){
    // 拿取
    arm_up();
    delay(1000);
    stepperX.step(4300 * -1);
}

void zero_to_entrance(){
    stepperX.step(4300);
}

void put_zero_position_zero(int pos){

    // 預設天車位置
    int x = 300 + ((pos - 1) * 500);
    int y = 2150;

    // 拿取
    arm_up();
    delay(1000);

    // 開始移動
    stepperX.step(x);
    stepperY.step(y);
    delay(1000); // 到定位

    // 放下
    arm_down();
    delay(1000);
    
    // 歸位
    stepperY.step(y * -1);
    stepperX.step(x * -1);

}


/*
Crane Position X List:
1: 300
2: 800
3: 1300
4: 1800
5: 2300
6: 2800
7: 3300
8: 3800
9: 4300

*/
