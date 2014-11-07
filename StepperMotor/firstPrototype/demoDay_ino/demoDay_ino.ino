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
long interval = 2500;
long intervalBounce = 700;

void setup(){
  pinMode (button, INPUT);
  Serial.begin(9600);
  
  AFMS.begin();
  myMotor->setSpeed(2);
}

void loop() {
  int reading = digitalRead(button);
   if (reading != lastButtonState) { //If current buttonstate has changed from last
    lastDebounceTime = millis(); 
  } 
  if ((millis() - lastDebounceTime) > debounceDelay) { //whatever the reading is, it has been there for
      if (reading != buttonState) { // longer than the debounce delay...
        buttonState = reading; // ...so take it as actual current state
        if (buttonState == HIGH) {
          buttonPushCounter++; // Increase the count by 1 with each loop/interval

          String stringOne = "buttonPushCounter: ";
          String stringThree = stringOne + buttonPushCounter;
          Serial.println(stringThree); }}}
          
  lastButtonState = reading; // Save current count as the last count for next time
  
 unsigned long currentMillis = millis(); // Don't stop code to wait (delay) but check if time passed
 if (currentMillis - previousMillis > interval) {
    previousMillis = currentMillis; }

     if (buttonPushCounter == 1) { // START ROTATING
      myMotor->step(20, FORWARD, SINGLE);
      myMotor->step(20, BACKWARD, SINGLE);
      Serial.println("Pressed");
    }
     if (buttonPushCounter == 2) { // ALL FLASHING
      myMotor->step(0, FORWARD, MICROSTEP); 
    }
           Serial.println(buttonPushCounter);
            
   if (buttonPushCounter > 3) {
       buttonPushCounter = 1; } 
}
  
