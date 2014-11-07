

#include <Wire.h>
#include <AFMotor.h>
#include "utility/Adafruit_PWMServoDriver.h"

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();  

// Connect a stepper motor with 200 steps per revolution (1.8 degree)
// to motor port #2 (M3 and M4)
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 1);
const int buttonPin = 9;
int buttonValue;

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Stepper 360");
  pinMode(buttonPin, INPUT);
  
  AFMS.begin();  // create with the default frequency 1.6KHz
  //AFMS.begin(1000);  // OR with a different frequency, say 1KHz
  
  myMotor->setSpeed(10);  // 10 rpm   
}

void loop() {
  
  buttonValue = digitalRead(buttonPin);
  Serial.println(buttonValue);
  //Serial.println("Microstep steps");
  if(buttonValue == LOW) {
    myMotor->step(1, FORWARD, MICROSTEP);
    Serial.println("Pressed");
    delay(400);
  }
  else{ 
    myMotor->step(0, FORWARD, MICROSTEP); }
  }
