int const trigPin = 13;
int const echoPin = 12;
int Duration;
int Distance;

void setup() {
    Serial.begin(9600);
    pinMode(trigPin, OUTPUT);
    pinMode(echoPin, INPUT);
    digitalWrite(trigPin, LOW);
}

int isTri = true, trigNow = 0, echoNow = 0;
void loop() {
    if (isTri == true) {
        digitalWrite(trigPin, HIGH);  //發射超音波
        isTri = false;
        trigNow = millis();
    } else if (isTri == false && millis() - trigNow >= 1000) {
        digitalWrite(trigPin, LOW);
        Duration = pulseIn(echoPin, HIGH);  //超音波發射到接收的時間
        Distance = Duration * 0.034 / 2;    //計算距離(cm)
        isTri = true;
    }
}