#include <Stepper.h>


const int disc_L298N1_In1 = 2; // 圓盤(步進馬達)的L298N in1
const int disc_L298N1_In2 = 3; // 圓盤(步進馬達)的L298N in2 
const int disc_L298N1_In3 = 4; // 圓盤(步進馬達)的L298N in3
const int disc_L298N1_In4 = 5; // 圓盤(步進馬達)的L298N in4

void setup()
{

    pinMode(disc_L298N1_In1, OUTPUT);
    pinMode(disc_L298N1_In2, OUTPUT);
    pinMode(disc_L298N1_In3, OUTPUT);
    pinMode(disc_L298N1_In4, OUTPUT);    
}

void loop()
{
    stepper_front(disc_L298N1_In1, disc_L298N1_In2, disc_L298N1_In3, disc_L298N1_In4);
}



void stepper_front(int In1, int In2, int In3, int In4) {

    int t = 2;

    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, HIGH);
    digitalWrite(In2, HIGH);
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, HIGH);
    digitalWrite(In3, LOW);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, HIGH);
    digitalWrite(In3, HIGH);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    digitalWrite(In3, HIGH);
    digitalWrite(In4, LOW);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    digitalWrite(In3, HIGH);
    digitalWrite(In4, HIGH);
    delay(t);

    digitalWrite(In1, LOW);
    digitalWrite(In2, LOW);
    digitalWrite(In3, LOW);
    digitalWrite(In4, HIGH);
    delay(t);

    digitalWrite(In1, HIGH);
    digitalWrite(In2, LOW);
    digitalWrite(In3, LOW);
    digitalWrite(In4, HIGH);
    delay(t); 

}

