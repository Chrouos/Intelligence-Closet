const int buttonPin1 = 22;  // 第一個按鈕腳位
const int buttonPin2 = 23;  // 第二個按鈕腳位
int buttonState1 = LOW;     // 第一個按鈕狀態
int buttonLastState1 = LOW; // 第一個按鈕上次狀態
long buttonLastDebounceTime1 = 0;  // 第一個按鈕上次彈跳時間
int buttonState2 = LOW;     // 第二個按鈕狀態
int buttonLastState2 = LOW; // 第二個按鈕上次狀態
long buttonLastDebounceTime2 = 0;  // 第二個按鈕上次彈跳時間
long debounceDelay = 50;    // 彈跳延遲時間

void setup() {
  pinMode(buttonPin1, INPUT_PULLUP);  // 設置第一個按鈕腳位為上拉輸入
  pinMode(buttonPin2, INPUT_PULLUP);  // 設置第二個按鈕腳位為上拉輸入
  Serial.begin(9600);  // 初始化序列通訊
}

void loop() {
  // 檢查第一個按鈕狀態
  if (checkTheBtnStatus(buttonPin1, buttonState1, buttonLastState1, buttonLastDebounceTime1, debounceDelay)) {
    Serial.println("Button 1 pressed!");  // 第一個按鈕被按下時顯示訊息
  }

  // 檢查第二個按鈕狀態
  if (checkTheBtnStatus(buttonPin2, buttonState2, buttonLastState2, buttonLastDebounceTime2, debounceDelay)) {
    Serial.println("Button 2 pressed!");  // 第二個按鈕被按下時顯示訊息
  }
}

int checkTheBtnStatus(const int button, int& buttonState, int& buttonLastState, long& buttonlastDebounceTime, long delayTime) {
  int buttonRead = digitalRead(button);
  if (buttonRead != buttonLastState) {  // 如果按鈕狀態和上次不同
    buttonlastDebounceTime = millis();  // 記錄初始時間
  }

  if ((millis() - buttonlastDebounceTime) > delayTime) {
    if (buttonRead != buttonState) {  // 如果按鈕狀態改變
      buttonState = buttonRead;

      // 切換到按下狀態
      if (buttonRead == HIGH) {
        return true;
      }
    }
  }
  buttonLastState = buttonRead;  // 保存處理結果
  return false;
}
