#include <IRremote.h>
#include <Servo.h>
#include <Stepper.h>

// ----- 步進馬達
Stepper stepperY(200, 2, 3, 4, 5);
Stepper stepperX(200, 8, 9, 10, 11);

// 雙軸伺服馬達
Servo biaxial_servo_x, biaxial_servo_y;
const int biaxial_servo_x_pin = A2, biaxial_servo_y_pin = A3;

// ----- 紅外遙控器
const int RECV_PIN = 47;
IRrecv irrecv(RECV_PIN);
decode_results results; // 紅外線接收訊號後會把結果存在 results
String strp, strnow;    //暫存器

// 參數
int mod = 0, donow = 0;                 //命令形式
int servo_x_pos = 50, servo_y_pos = 50; //手臂位置
int angle = 1, angle_delayTime = 15;    //手臂必要參數
int CraneX = 0, CraneY = 0;             // 實際天車的 Direct
int CranxDirect_Up = -50, CranxDirect_Down = 50, CranxDirect_Left = 50,
    CranxDirect_Right = -50;

// 按鈕設定
const int x_StopButton = 23; // x 軸歸零
const int y_StopButton = 22;  // y 軸歸零

long globalDelayTime = 50;  // 消斗的時間

int x_StopButtonState; // 入口微動開關的狀態
int x_StopButtonLastState = LOW; // 入口微動開關的最後狀態
long x_StopButtonlastDebounceTime = 0;  // 按了最後一次被觸發
int y_StopButtonState; // 入口微動開關的狀態
int y_StopButtonLastState = LOW; // 入口微動開關的最後狀態
long y_StopButtonlastDebounceTime = 0;  // 按了最後一次被觸發


void setup() {
  Serial.begin(9600);
  Serial.println("Start");

  // 按鈕設定
  pinMode(x_StopButton, INPUT);
  pinMode(y_StopButton, INPUT);

  // 伺服馬達
  //  biaxial_servo_x.attach(biaxial_servo_x_pin); // 雙軸 X
  //  biaxial_servo_y.attach(biaxial_servo_y_pin); // 雙軸 Y

  // ----- 紅外遙控器
  irrecv.enableIRIn(); // 開始接收訊號！

  // ----- 步進馬達，將馬達速度設定為每分鐘 120 轉(RPM)
  stepperX.setSpeed(80);
  stepperY.setSpeed(80);

  arm_down();
  delay(1000);

  Serial.println("Please Start Now ....");
}

void loop() {

  if (Serial.available()) {

    char pos = Serial.read();
    if(pos == 'z'){
      Serial.println("歸零指令: " + String(pos) );
      correction_zero();
    }
    else if (pos >= '1' && pos <= '9'){
      Serial.println("位置: " + String(pos) );
      position_test(pos - '0');
    }
    pos = '0';
  }
}

void correction_zero(){

  int run_return_x = -25, run_return_y = -25;

  // (1) 先將 y 拖回來
  while (run_return_y != 0){
    // 是否到底(停下) Y
    if( checkTheBtnStatus( y_StopButton, y_StopButtonState, y_StopButtonLastState, y_StopButtonlastDebounceTime, globalDelayTime) == true
    ){
        run_return_y = 0;
        Serial.println("碰到微動開關 Y 停止");
    }
    stepperY.step(run_return_y);
  }

  // (2) 再將 x 拖回來  
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


void position_test(int pos){
  int x = 300 + ((pos - 1) * 500);
  int y = 2150;

  arm_down();

  stepperX.step(x);
  stepperY.step(y);

  delay(1000);
  arm_up();
  delay(1000);
  arm_down();

  delay(1000);
  stepperY.step(y * -1);
  stepperX.step(x * -1);
}

// ----------------- 手臂 v ----------------- //
void arm_left() { //手臂左轉
  Serial.println("手臂向左");
  while (servo_x_pos + (-1 * angle) >= 0) {
    servo_x_pos += (-1 * angle);
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_x.write(servo_x_pos);
    delay(angle_delayTime * 2);
  }
}
void arm_right() { //手臂右轉
  Serial.println("手臂向右");
  while (servo_x_pos + (1 * angle) <= 92) {
    servo_x_pos += (1 * angle);
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_x.write(servo_x_pos);
    delay(angle_delayTime);
  }
}
void arm_down() { //手臂放下
  Serial.println("手臂向下");
  while (servo_y_pos + (1 * angle) <= 62) {
    servo_y_pos += (1 * angle);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    biaxial_servo_y.write(servo_y_pos);
    delay(angle_delayTime * 2);
  }
}
void arm_up() { //手臂勾起
  Serial.println("手臂向上");
  while (servo_y_pos + (-1 * angle) >= 42) {
    servo_y_pos += (-1 * angle);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    biaxial_servo_y.write(servo_y_pos);
    delay(angle_delayTime * 2);
  }
}
// ----------------- 手臂 ^ ----------------- //

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
