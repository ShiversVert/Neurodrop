#include <MultiStepper.h>
#include <AccelStepper.h>

// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver:
#define dirPin 10
#define stepPin 11
#define motorInterfaceType 1
// Create a new instance of the AccelStepper class:
AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);
void setup() {
  // Set the maximum speed and acceleration:
  Serial.begin(9600);
  Serial.println("Begin");
  stepper.setMaxSpeed(3500);
  stepper.setAcceleration(500);
  Serial.println("Initialization done");
}
void loop() {
  Serial.println("Move to 50000");
  stepper.moveTo(50000);
  stepper.runToPosition();
  delay(1000);
  Serial.println("Move to 0");
  stepper.moveTo(0);
  stepper.runToPosition();
  delay(1000);
}
