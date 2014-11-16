#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();  
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 1);

const int button =9; //button input spot
long previousMillis = 0;
long currentMillis = millis();
int val = 0 ;

int buttonState; 
int buttonPushCounter = 0; // Count of presses
int lastButtonState = LOW; // previous state (HIGH or LOW) of button

long lastDebounceTime = 0;
long debounceDelay = 50; // time necessary for intentional press
long interval = 1000;
long intervalBounce = 400;

void setup(){
  pinMode (button, INPUT);
  Serial.begin(9600);
  
  AFMS.begin();
  myMotor->setSpeed(2);
}

void loop() {
  Serial.print("Unce more through the loop");
  int reading = digitalRead(button);
   Serial.print(reading);
  
     if (reading==HIGH) { // START ROTATING
      myMotor->step(4, FORWARD, SINGLE);
      Serial.println("Pressed");
      delay(1000);
    }
  
}
