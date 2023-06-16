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
int CranxDirect_Up = -50, CranxDirect_Down = 50, CranxDirect_Left = 50, CranxDirect_Right = -50;

int axis_x = 0, axis_y = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Start");

  // 伺服馬達
  biaxial_servo_x.attach(biaxial_servo_x_pin); // 雙軸 X
  biaxial_servo_y.attach(biaxial_servo_y_pin); // 雙軸 Y

  // ----- 紅外遙控器
  irrecv.enableIRIn(); // 開始接收訊號！

  // ----- 步進馬達，將馬達速度設定為每分鐘 120 轉(RPM)
  stepperX.setSpeed(80);
  stepperY.setSpeed(80);
}

void loop() {

  if (irrecv.decode(&results)) {
    // Serial.println(results.value);
    if (results.value == 4294967295) { // 最大值接收到重复值
      strnow = strp;
    } else {
      strnow = results.value;
      strp = results.value;
    }

    // --------------------------- setting 數字鍵
    if (strnow == "16736925") { // 2:前
      CraneY = CranxDirect_Down;
      axis_y += CraneY; // 紀錄座標 y
      Serial.println("前");
      Serial.println("axis_x:" + String(axis_x) + ", axis_y:" + String(axis_y) );
    } else if (strnow == "16720605") { // 4:左
      CraneX = CranxDirect_Left;
      axis_x += CraneX; // 紀錄座標 x
      Serial.println("axis_x:" + String(axis_x) + ", axis_y:" + String(axis_y) );
      Serial.println("左");
    } else if (strnow == "16761405") { // 6:右
      CraneX = CranxDirect_Right;
      axis_x += CraneX; // 紀錄座標 x 
      Serial.println("axis_x:" + String(axis_x) + ", axis_y:" + String(axis_y) );
      Serial.println("右");
    } else if (strnow == "16754775") { // 8:後
      CraneY = CranxDirect_Up;
      axis_y += CraneY; // 紀錄座標 y 
      Serial.println("axis_x:" + String(axis_x) + ", axis_y:" + String(axis_y) );
      Serial.println("後");
    }

    // --------------------------- setting 上下左右

    if (strnow == "16718055") { //手臂向下
      arm_down();
    }
    if (strnow == "16730805") { //手臂向上
      arm_up();
    }
    if (strnow == "16734885") { //手臂向右
      arm_right();
    }
    if (strnow == "16716015") { //手臂向左
      arm_left();
    }

    irrecv.resume(); // 接著接收下一個訊號
  }

  // 沒有按鍵的情況下，所有歸零(不動)
  else {
    CraneX = 0;
    CraneY = 0;
  }
  // 結束
  stepperX.step(CraneX);
  stepperY.step(CraneY);
  // Serial.println(String(CraneX) + " " + String(CraneY));
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
void arm_up() { //手臂勾起
  Serial.println("手臂向上");
  while (servo_y_pos + (1 * angle) <= 62) {
    servo_y_pos += (1 * angle);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    biaxial_servo_y.write(servo_y_pos);
    delay(angle_delayTime * 2);
  }
}
void arm_down() { //手臂放下
  Serial.println("手臂向下");
  while (servo_y_pos + (-1 * angle) >= 42) {
    servo_y_pos += (-1 * angle);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    biaxial_servo_y.write(servo_y_pos);
    delay(angle_delayTime * 2);
  }
}
// ----------------- 手臂 ^ ----------------- //
