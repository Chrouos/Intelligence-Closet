#include <IRremote.h>
#include <LiquidCrystal_I2C.h>  // LCD_I2C模組程式庫
#include <Servo.h>
#include <Stepper.h>

// 雙軸伺服馬達
Servo biaxial_servo_x, biaxial_servo_y; 
const int biaxial_servo_x_pin = A1, biaxial_servo_y_pin = A2; 
// 車車的伺服馬達
Servo car_servo;
const int car_servo_pin = A6;
// 入口的伺服馬達
Servo entrance_servo;
const int entrance_servo_pin = A5;
// LCD
LiquidCrystal_I2C lcd(0x27, 16, 4); // I2C位址，默認為0x27或0x3F，依據背板的晶片不同而有差異，16、2為LCD顯示器大小。
// ----------------------------- 控制腳位 start ----------------------------- //
//紅外遙控器
const int RECV_PIN = 53;
IRrecv irrecv(RECV_PIN);
decode_results results;//接收訊號後會把結果存在results
String strp,strnow;//暫存器
int mod=0,donow=0;//命令形式

// 伺服馬達
int servo_x_lastStatus = false, servo_y_lastStatus = false, servo_entrance_lastStatus = false;
// 車車(減速馬達)的L298N
const int entrance_L298N_car[4] = {6, 7, 8, 9};
int car_lastState = false;
//步進馬達
Stepper disc_stepper(200, 2, 3, 4, 5); 
const int disc_btn_front = 24, discButton = 23, disc_btn_back = 22;
const int relay = 48; // 繼電器
int disc_lastState = false;

int car_servo_lastStatus = false;

int servo_x_pos = 12, servo_y_pos = 40, servo_car_pos =100, servo_entrance_pos = 20;
int angle = 1, angle_delayTime = 15;

int discButtonState; // 圓盤微動開關的狀態
int discButtonLastState = LOW; // 圓盤微動開關的最後狀態
long discButtonlastDebounceTime = 0;  // 按了最後一次被觸發
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
    pinMode(disc_btn_front, INPUT);
    pinMode(disc_btn_back, INPUT);
    pinMode(discButton, INPUT);
    
    for(int i=0; i<4; i++){
        pinMode(entrance_L298N_car[i], OUTPUT);
    }

    // 伺服馬達
    biaxial_servo_x.attach(biaxial_servo_x_pin); // 雙軸 X
    biaxial_servo_y.attach(biaxial_servo_y_pin); // 雙軸 Y
    car_servo.attach(car_servo_pin); 
    entrance_servo.attach(entrance_servo_pin); // 入口 伺服馬達
    // 伺服馬達定位
    biaxial_servo_x.write(0);
    biaxial_servo_y.write(0);
    car_servo.write(100);
    entrance_servo.write(0);


    // 步進馬達
    pinMode(relay, OUTPUT);
    digitalWrite(relay, LOW);
    disc_stepper.setSpeed(5);

    // 初始化 LCD
    lcd.init();
    lcd.backlight();
    lcd.clear();
    setUpLCD(1, 3, "test mode");
    
    
    // 最後歸位
    delay(1000);
    biaxial_servo_x.detach();
    biaxial_servo_y.detach();
    car_servo.detach();
    entrance_servo.detach();

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
    setUpLCD(1, 3, "car control");
    Serial.println("1");}
  if(strnow=="16736925"){
    mod=2;
    setUpLCD(1, 3, "arm control");
    Serial.println("2");}
  if(strnow=="16769565"){
    mod=3;
    setUpLCD(1, 3, "door control");
    Serial.println("3");}
  if(strnow=="16720605"){
    mod=4;
    setUpLCD(1, 3, "mid control");
    Serial.println("4");}
////////////////////////////////////////////////////////////////////////執行命令
  if(mod==1){//車車控制
    if(strnow=="16718055"){//車車勾起
        car_up();
      }
    if(strnow=="16730805"){//車車放下
        car_down();
      }
    if(strnow=="16734885"){//車車前進
      car_go(entrance_L298N_car);
      }
    if(strnow=="16716015"){//車車後退
      car_back(entrance_L298N_car);
      }
  }

  if(mod==2){//手臂控制
    if(strnow=="16718055"){//手臂向上
      arm_up();
      }
    if(strnow=="16730805"){//手臂向下
      arm_down();
      }
    if(strnow=="16734885"){//手臂向右
      arm_right();
      }
    if(strnow=="16716015"){//手臂向左
      arm_left();
      }
  }

  if(mod==3){//入口伺服馬達
    if(strnow=="16718055"){
      Serial.println("3上");
      park_up();
    }
    if(strnow=="16730805"){
      Serial.println("3下");
      park_down();
    }
  }

  if(mod==4){//圓盤控制
    if(strnow=="16726215"){//OK
      Serial.println("轉動");
      }
    if(strnow=="16718055"){//上
      Serial.println("轉1個位置");
      setUpLCD(1, 3, "turn 1");
      digitalWrite(relay, HIGH);
      discRotate_withTimes(1);
      delay(2000);
      digitalWrite(relay, LOW);
      }
    if(strnow=="16730805"){//下
      Serial.println("轉2個位置");
      setUpLCD(1, 3, "turn 2");
      digitalWrite(relay, HIGH);
      discRotate_withTimes(2);
      delay(2000);
      digitalWrite(relay, LOW);
      }
    if(strnow=="16716015"){//左
      Serial.println("轉3個位置");
      setUpLCD(1, 3, "turn 3");
      digitalWrite(relay, HIGH);
      discRotate_withTimes(3);
      delay(2000);
      digitalWrite(relay, LOW);
      }
    if(strnow=="16734885"){//右
      Serial.println("轉4個位置");
      setUpLCD(1, 3, "turn 4");
      digitalWrite(relay, HIGH);
      discRotate_withTimes(4);
      delay(2000);
      digitalWrite(relay, LOW);
      }
    if(strnow=="16712445"){//5
      Serial.println("轉5個位置");
      setUpLCD(1, 3, "turn 5");
      digitalWrite(relay, HIGH);
      discRotate_withTimes(5);
      delay(2000);
      digitalWrite(relay, LOW);
      }
    if(strnow=="16761405"){//6
      Serial.println("轉6個位置");
      setUpLCD(1, 3, "turn 6");
      digitalWrite(relay, HIGH);
      discRotate_withTimes(6);
      delay(2000);
      digitalWrite(relay, LOW);
      }
    if(strnow=="16769055"){//7
      Serial.println("轉7個位置");
      setUpLCD(1, 3, "turn 7");
      digitalWrite(relay, HIGH);
      discRotate_withTimes(7);
      delay(2000);
      digitalWrite(relay, LOW);
      }
  }

////////////////////////////////////////////////////////////////////////編碼
//    if(strnow=="16753245"){Serial.println("1");}
//    if(strnow=="16736925"){Serial.println("2");}
//    if(strnow=="16769565"){Serial.println("3");}
//    if(strnow=="16720605"){Serial.println("4");}
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
    car_stop(entrance_L298N_car);
    car_lastState = false;
  }
  if(car_servo_lastStatus == true){
    car_servo.detach();
    car_servo_lastStatus = false;
  }
  if(servo_x_lastStatus == true){
  biaxial_servo_x.detach();
  servo_x_lastStatus = false;
  }
  if(servo_y_lastStatus == true){
  biaxial_servo_y.detach();
  servo_y_lastStatus = false;
  }
  if(servo_entrance_lastStatus == true){
  entrance_servo.detach();
  servo_entrance_lastStatus = false;
  }
  delay(150);
}
}
// ------------------------------ 控制 End ------------------------------ //

// -----------------入口停車場----------------- //
void park_up(){
  Serial.println("入口伺服往上");
  while(servo_entrance_pos + (1 * angle) <= 135 ){
    servo_entrance_pos += (1 * angle);
    entrance_servo.attach(entrance_servo_pin);
    entrance_servo.write(servo_entrance_pos);
    delay(angle_delayTime * 2);
  }
  Serial.println("servo_entrance_pos: " + String(servo_entrance_pos));
  setUpLCD(1, 0, "Park: "  + String(servo_entrance_pos) + " ");
  servo_entrance_lastStatus = true;
}
void park_down(){
  Serial.println("入口伺服往下");
  while(servo_entrance_pos + (-1 * angle) >= 0 ){
    servo_entrance_pos += (-1 * angle);
    entrance_servo.attach(entrance_servo_pin);
    entrance_servo.write(servo_entrance_pos);
    delay(angle_delayTime * 2);
  }
  Serial.println("servo_entrance_pos: " + String(servo_entrance_pos));
  setUpLCD(1, 0, "Park: "  + String(servo_entrance_pos) + " ");
  servo_entrance_lastStatus = true;

  
  
}


// -----------------手臂----------------- //
//手臂左轉
void arm_left(){
  Serial.println("手臂向左");
  while(servo_x_pos + (-1 * angle) >= 12 ){
    servo_x_pos += (-1 * angle);
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_x.write(servo_x_pos);
    delay(angle_delayTime*2);
  }
  Serial.println("servo_x_pos: " + String(servo_x_pos));
  setUpLCD(1, 0, "X: "  + String(servo_x_pos) + " ");
  servo_x_lastStatus = true;
}
//手臂右轉
void arm_right(){
  Serial.println("手臂向右");
  while(servo_x_pos + (1 * angle) <= 75 ){
    servo_x_pos += (1 * angle);
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_x.write(servo_x_pos);
    delay(angle_delayTime);
  }
  delay(1000);
  while(servo_x_pos + (1 * angle) <= 101 ){
    servo_x_pos += (1 * angle);
    biaxial_servo_x.attach(biaxial_servo_x_pin);
    biaxial_servo_x.write(servo_x_pos);
    delay(angle_delayTime*2);
  }
  Serial.println("servo_x_pos: " + String(servo_x_pos));
  setUpLCD(1, 0, "X: "  + String(servo_x_pos) + " ");
  servo_x_lastStatus = true;
}
//手臂勾起
void arm_up(){
  Serial.println("手臂向上");
  while(servo_y_pos + (1 * angle) <= 155 ){
    servo_y_pos += (1 * angle);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    biaxial_servo_y.write(servo_y_pos);
    delay(angle_delayTime*2);
  }
  Serial.println("servo_y_pos: " + String(servo_y_pos));
  setUpLCD(1, 1, "Y: "  + String(servo_y_pos) + " ");
  servo_y_lastStatus = true;
}
//手臂放下
void arm_down(){
  Serial.println("手臂向下");
  while(servo_y_pos + (-1 * angle) >= 30 ){
    servo_y_pos += (-1 * angle);
    biaxial_servo_y.attach(biaxial_servo_y_pin);
    biaxial_servo_y.write(servo_y_pos);
    delay(angle_delayTime*2);
  }
  Serial.println("servo_y_pos: " + String(servo_y_pos));
  setUpLCD(1, 1, "Y: "  + String(servo_y_pos) + " ");
  servo_y_lastStatus = true;
}
// -----------------車車----------------- //
// 步進馬達: 停止
void car_stop(int l298n_car[4]) {
    digitalWrite(l298n_car[0], LOW);
    digitalWrite(l298n_car[1], LOW);
    digitalWrite(l298n_car[2], LOW);
    digitalWrite(l298n_car[3], LOW);
}
// 步進馬達: 前進
void car_go(int l298n_car[4]) {
    Serial.println("車車前進");
    digitalWrite(l298n_car[0], LOW);
    digitalWrite(l298n_car[1], HIGH);
    digitalWrite(l298n_car[2], LOW);
    digitalWrite(l298n_car[3], HIGH);
    car_lastState = true;
}
// 步進馬達: 後退
void car_back(int l298n_car[4]) {
    Serial.println("車車後退"); 
    digitalWrite(l298n_car[0], HIGH);
    digitalWrite(l298n_car[1], LOW);
    digitalWrite(l298n_car[2], HIGH);
    digitalWrite(l298n_car[3], LOW);
    car_lastState = true;
}
//車車勾起
void car_up(){
  Serial.println("車車勾住");
  while(servo_car_pos + (1 * angle) <= 164 ){
    servo_car_pos += (1 * angle);
    car_servo.attach(car_servo_pin);
    car_servo.write(servo_car_pos);
    delay(angle_delayTime);
  }
  car_servo_lastStatus = true;
  Serial.println("servo_car_pos: " + String(servo_car_pos));
  setUpLCD(1, 2, "car: "  + String(servo_car_pos) + " ");
}
//車車放下
void car_down(){
  Serial.println("車車放下");
  while(servo_car_pos + (-1 * angle) >= 100 ){
    servo_car_pos += (-1 * angle);
    car_servo.attach(car_servo_pin);
    car_servo.write(servo_car_pos);
    delay(angle_delayTime);
    }
  car_servo_lastStatus = true;
  Serial.println("servo_car_pos: " + String(servo_car_pos));
  setUpLCD(1, 2, "car: "  + String(servo_car_pos) + " ");
}
// -----------------LCD----------------- //
// LCD 顯示畫面
void setUpLCD(int column, int row, String text){
    lcd.setCursor(column, row);  // (colum, row) 
    lcd.print(text);
}
// -----------------圓盤----------------- //
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
//圓盤轉動
void discRotate_withTimes(int times){
  long globalDelayTime = 50;  // 消斗的時間

    Serial.println("discRotate_withTimes have to rotate " + String(times) + " Times");
    long temp_time = millis();
    int now_times = 0;
    // 開始旋轉 
    
    bool disc_start = true;  // true: start, false: stop
    //disc_start == true | now_times <= times
    while( now_times != times){

        disc_stepper.step(-1);  // 20/200 = 1/10
        if(millis() - temp_time > 500){
          if( checkTheBtnStatus(discButton, discButtonState, discButtonLastState, discButtonlastDebounceTime, globalDelayTime) == true){
              disc_start = false;
              now_times++;
          }
        }
       
    }
    // 微動開關按了才結束
}
