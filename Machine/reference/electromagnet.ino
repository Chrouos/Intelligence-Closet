int electromagnetPin = 45; // 電磁鐵
void setup()
{
  pinMode(electromagnetPin, OUTPUT); // 設定 pin 3 為輸出
}
// 下面這個 loop 會讓 LED 燈由暗變為一半亮度，最後變成最大亮度
void loop()
{
    analogWrite(electromagnetPin, 255);  // LED 最大亮度
    delay (1000);
}