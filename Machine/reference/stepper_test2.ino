
#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution

Stepper myStepper(stepsPerRevolution, 2, 3, 4, 5);

void setup() {
  myStepper.setSpeed(60);
  Serial.begin(9600);
}

void loop() {
  Serial.println("front");
  myStepper.step(stepsPerRevolution);
  delay(1000);

  Serial.println("back");
  myStepper.step(-stepsPerRevolution);
  delay(1000);
}
