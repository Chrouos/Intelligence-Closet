#include <IRremote.h>
#include <Stepper.h>

// ----- 步進馬達
Stepper stepperY(200, 2, 3, 4, 5);
Stepper stepperX(200, 8, 9, 10, 11);

// ----- 紅外遙控器
const int RECV_PIN = 49;
IRrecv irrecv(RECV_PIN);
decode_results results; // 紅外線接收訊號後會把結果存在 results
String strp, strnow;    //暫存器
int mod = 0, donow = 0; //命令形式

void setup() {
  Serial.begin(9600);
  Serial.println("Start");

  // ----- 紅外遙控器
  irrecv.enableIRIn(); // 開始接收訊號！

  // ----- 步進馬達，將馬達速度設定為每分鐘 120 轉(RPM)
  stepperX.setSpeed(120);
  stepperY.setSpeed(120);
}

int CraneX = 0, CraneY = 0;
void loop() {

  if (irrecv.decode(&results)) {

    if (results.value == 4294967295) { //最大值接收到重复值
      strnow = strp;
    } else {
      strnow = results.value;
      strp = results.value;
    }

    // --------------------------- setting 數字鍵
    if (strnow == "16753245") { // 1: 右上
      CraneX = -50;
      CraneY = -50;
    }
    else if (strnow == "16736925"){ // 2: 上
      CraneY = -50;
    }
    else if (strnow == "16736925"){ // 3: 左上
      CraneX = 50;
      CraneY = -50;

    }
    else if (strnow == "16736925"){ // 4: 左
      CraneX = 50;
    }
    else if (strnow == "16736925"){ // 5: 

    }
    else if (strnow == "16736925"){ // 6: 右
      CraneX = -50;
    }
    else if (strnow == "16736925"){ // 7: 左下
      CraneX = 50;
      CraneY = 50;
    }
    else if (strnow == "16736925"){ // 8: 下
      CraneY = 50;
    }
    else if (strnow == "16736925"){ // 9: 右下
      CraneX = -50;
      CraneY = 50;
    }
  

    // --------------------------- setting 上下左右

    // 上
    if (strnow == "16718055") {
    }

    // 下
    if (strnow == "16730805") {
    }

    // 右
    if (strnow == "16734885") {
    }

    // 左
    if (strnow == "16716015") {
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
  Serial.println(String(CraneX) + " " + String(CraneY));
}
