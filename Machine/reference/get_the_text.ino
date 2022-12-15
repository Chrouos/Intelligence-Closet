#define LED 13
String str;

void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        // 讀取傳入的字串直到"\n"結尾
        str = Serial.readStringUntil('\n');

        if (str == "GO_Storage") {
            Serial.println("GO Storage");
        } else if (str == "GO_PickUp") {
            Serial.println("GO PickUp");
        }
    }
}
