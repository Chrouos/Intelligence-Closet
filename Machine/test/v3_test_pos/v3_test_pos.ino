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

int mod = 0, donow = 0;                 //命令形式
int servo_x_pos = 50, servo_y_pos = 50; //手臂位置
int angle = 1, angle_delayTime = 15;    //手臂必要參數
int CraneX = 0, CraneY = 0;             // 實際天車的 Direct
int CranxDirect_Up = -50, CranxDirect_Down = 50, CranxDirect_Left = 50,
    CranxDirect_Right = -50;

int now_x = 0, now_y = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Start");

  // 伺服馬達
  //  biaxial_servo_x.attach(biaxial_servo_x_pin); // 雙軸 X
  //  biaxial_servo_y.attach(biaxial_servo_y_pin); // 雙軸 Y

  // ----- 紅外遙控器
  irrecv.enableIRIn(); // 開始接收訊號！

  // ----- 步進馬達，將馬達速度設定為每分鐘 120 轉(RPM)
  stepperX.setSpeed(80);
  stepperY.setSpeed(80);
}

void loop() {

  if (Serial.available()) {

    char pos = Serial.read();
    Serial.println("pos:" + String(pos));
    position_test(pos);
    
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
