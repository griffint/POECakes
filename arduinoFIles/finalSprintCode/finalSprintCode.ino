//Final Arduino Code for Cakebot
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotor = AFMS.getMotor(3);
Adafruit_StepperMotor *linearMotor = AFMS.getStepper(200,1);

//code here to initialize all digital input ports


void setup() {
  AFMS.begin();
  myMotor->setSpeed(250);
  linearMotor->setSpeed(30);
  Serial.begin(9600);

  pinMode(platformStep,OUTPUT);
}


void loop(){
 //serial print to 
  
}

void turnFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds
  
}

void moveTopFroster(int steps, int directions){ //this moves the top frosting motor given # of steps
  
}

void spinPlatform(int steps, int directions){ //this spins the cake platform given # of steps

}
