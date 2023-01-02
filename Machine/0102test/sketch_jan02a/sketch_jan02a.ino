#include <IRremote.h>
#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Stepper.h>

// 雙軸伺服馬達
Servo biaxial_servo_x, biaxial_servo_y; 
const int biaxial_servo_x_pin = A1, biaxial_servo_y_pin = A2; 
// 車車的伺服馬達
Servo car_servo;
const int car_servo_pin = A4;
// LCD
LiquidCrystal_I2C lcd(0x27, 16, 4); // I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、2為LCD顯示器大小。
// ----------------------------- 控制腳位 end ----------------------------- //
//紅外遙控器
const int RECV_PIN = 53;
IRrecv irrecv(RECV_PIN);
decode_results results;//接收訊號後會把結果存在results
String strp,strnow;//暫存器
int mod=0,donow=0;//命令形式

// 伺服馬達
const int biaxial_servo_x_control_btn_negative = 27, biaxial_servo_x_control_btn_positive = 25;
const int biaxial_servo_y_control_btn_negative = 31, biaxial_servo_y_control_btn_positive = 29;
int servo_x_lastStatus = false, servo_y_lastStatus = false;
// 車車(減速馬達)的L298N
const int entrance_L298N_car[4] = {6, 7, 8, 9};
const int car_front_btn = 33, car_back_btn = 35;
int car_lastState = false;
//步進馬達
// Stepper disc_stepper(200, 2, 3, 4, 5); 
// const int disc_btn_front = 39, disc_btn_back = 37;
// const int relay = 48; // 繼電器
// int disc_lastState = false;
// 車車的伺服馬達(掛勾)
const  int car_servo_btn_negative = 39, car_servo_btn_positive = 37;
int car_servo_lastStatus = false;

int servo_x_pos = 0, servo_y_pos = 0, servo_car_pos = 0;
int angle = 1, angle_delayTime = 15;

// ----------------------------- 控制腳位 end ----------------------------- //
// ------------------------------ 變數設定 ------------------------------ //
void setup() {

    // 開啟Serial Port 並設定通訊速率(baud rate) 
    Serial.begin(9600); 
    
    //紅外遙控器
    Serial.println("Enabling IRin");
    irrecv.enableIRIn(); // 開始接收訊號！
    Serial.println("Enabled IRin");
    
    // 控制腳位
    pinMode(biaxial_servo_x_control_btn_negative, INPUT);
    pinMode(biaxial_servo_x_control_btn_positive, INPUT);
    pinMode(biaxial_servo_y_control_btn_negative, INPUT);
    pinMode(biaxial_servo_y_control_btn_positive, INPUT);
    pinMode(car_front_btn, INPUT);
    pinMode(car_back_btn, INPUT);

    pinMode(car_servo_btn_negative, INPUT);
    pinMode(car_servo_btn_positive, INPUT);
    // pinMode(disc_btn_front, INPUT);
    // pinMode(disc_btn_back, INPUT);
    
    for(int i=0; i<4; i++){
        pinMode(entrance_L298N_car[i], OUTPUT);
    }

    // 伺服馬達
    biaxial_servo_x.attach(biaxial_servo_x_pin); // 雙軸 X
    biaxial_servo_y.attach(biaxial_servo_y_pin); // 雙軸 Y
    car_servo.attach(car_servo_pin); 
    // 伺服馬達定位
    biaxial_servo_x.write(0);
    biaxial_servo_y.write(0);
    car_servo.write(100);

    // 步進馬達
//    pinMode(relay, OUTPUT);
//    digitalWrite(relay, LOW);
//    disc_stepper.setSpeed(30);

    // 初始化 LCD
    lcd.init();
    lcd.backlight();
    lcd.clear();

    //setUpLCD(1, 3, "test mode");
    
    
    // 最後歸位
    delay(1000);
    biaxial_servo_x.detach();
    biaxial_servo_y.detach();
    car_servo.detach();

}

// ------------------------------ 控制 Start ------------------------------ //
void loop() {
  if (irrecv.decode(&results)) {
    //Serial.println(results.value, HEX); //接收訊號，以16進位型式輸出到監控視窗
    //Serial.println("------------");
    if(results.value==4294967295){//最大值接收到重复值
        strnow=strp;
      }else{
        strnow=results.value;
        strp=results.value;
      }
////////////////////////////////////////////////////////////////////////模式調整
    if(strnow=="16753245"){
      mod=1;
      Serial.println("1");}
    if(strnow=="16736925"){
      mod=2;
      Serial.println("2");}
    if(strnow=="16769565"){
      mod=3;
      Serial.println("3");}
    if(strnow=="16720605"){
      mod=4;
      Serial.println("4");}
////////////////////////////////////////////////////////////////////////
    if(mod==1){
      if(strnow=="16718055"){//車車伺服正
        Serial.println("車車勾住");
        if(servo_car_pos + (1 * angle) <= 180 ){
          servo_car_pos += (1 * angle);
          car_servo.attach(car_servo_pin);
          car_servo.write(servo_car_pos);
          delay(angle_delayTime);
        }
        Serial.println("servo_car_pos: " + String(servo_car_pos));
      }
      if(strnow=="16730805"){
        Serial.println("車車放下");
        if(servo_car_pos + (-1 * angle) >= 0 ){
          servo_car_pos += (-1 * angle);
          car_servo.attach(car_servo_pin);
          car_servo.write(servo_car_pos);
          delay(angle_delayTime);
      }
        Serial.println("servo_car_pos: " + String(servo_car_pos));
        }
      if(strnow=="16716015"){//車車伺服負
        Serial.println("車車後退");
        mback(entrance_L298N_car);
        Serial.println("car front. ");
        car_lastState = true;
      }
      if(strnow=="16734885"){//車車前進
        Serial.println("車車前進");
        mfront(entrance_L298N_car);
        Serial.println("car back. ");
        car_lastState = true;
      }
    }
    if(mod==2){
      if(strnow=="16718055"){Serial.println("2上");}
      if(strnow=="16730805"){Serial.println("2下");}
      if(strnow=="16716015"){Serial.println("2左");}
      if(strnow=="16734885"){Serial.println("2右");}
    }
    if(mod==3){
      if(strnow=="16718055"){Serial.println("1上");}
      if(strnow=="16730805"){Serial.println("1下");}
    }
    if(mod==4){
      if(strnow=="16726215"){Serial.println("OK");}
      if(strnow=="16718055"){Serial.println("4上");}
      if(strnow=="16730805"){Serial.println("4下");}
      if(strnow=="16716015"){Serial.println("4左");}
      if(strnow=="16734885"){Serial.println("4右");}
      if(strnow=="16712445"){Serial.println("4五");}
      if(strnow=="16761405"){Serial.println("4六");}
      if(strnow=="16769055"){Serial.println("4七");}
    }
////////////////////////////////////////////////////////////////////////
//    if(strnow=="16712445"){Serial.println("5");}
//    if(strnow=="16761405"){Serial.println("6");}
//    if(strnow=="16769055"){Serial.println("7");}
//    if(strnow=="16754775"){Serial.println("8");}
//    if(strnow=="16748655"){Serial.println("9");}
//    if(strnow=="16750695"){Serial.println("0");}
//    if(strnow=="16718055"){Serial.println("上");}
//    if(strnow=="16730805"){Serial.println("下");}
//    if(strnow=="16716015"){Serial.println("左");}
//    if(strnow=="16734885"){Serial.println("右");}
//    if(strnow=="16726215"){Serial.println("OK");}
////////////////////////////////////////////////////////////////////////
    strnow="";
    irrecv.resume(); // 接著接收下一個訊號
    delay(150);
  }
  else {
    if(car_lastState == true){
      mstop(entrance_L298N_car);
      car_lastState = false;
    }
  }
}
// ------------------------------ 控制 End ------------------------------ //
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
