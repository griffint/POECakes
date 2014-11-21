//POE CakeBot Team Code
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_DCMotor *myMotor = AFMS.getMotor(1);
//code for motor shield stepper motor here

//also need code to initialize input ports for switches
int platformStep = 7;


void setup() {
  AFMS.begin();
  myMotor->setSpeed(200);
  Serial.begin(9600);

  pinMode(platformStep,OUTPUT);
}


void loop() {
  turnPlatform(200,0);
  delay(2000);
  //motor check code
  
  //button press code here
  
  //printing design code here 
  
}

void turnFrostingMotor(int time, int directions){
 //this will turn the frosting motor for a given time
 //directions will be 0 or 1
 myMotor->setSpeed(100);
 int startTime=0;
 int currentTime = 0;
 startTime=millis();
 while(currentTime-startTime<1000){
   myMotor->run(FORWARD);
   int currentTime = millis();
 }
}


void turnlinearStepper(int steps, int directions){
  //this will turn the linear actuation motor the given number of steps
  //directions will be 0 or 1
  //this motor will use the adafruit library
  
} 


//=============this guy will turn a step command into the commands the stepper motor===
//=================connected to the platform motor needs=================
void turnPlatform(int steps, int directions){
  //directions will be 0 or 1
  //this motor will use the pololu driver, so will need to use individual steps
  //pin 7 for step 8 for direction
 int stepCounter = steps;
  while (stepCounter>0){
    digitalWrite(platformStep, HIGH);
    stepCounter -= 1;
  }
}
  
  
void testConnect(){
  //this code will read from serial to test the connection to cakebot desktop
  char incomingByte = 0;
  //myMotor->run(FORWARD);
  
  //connection testing code here
  //can use serial.available to check if there's any data to read
  //serial receive buffer can hold 64 bytes of data
  if (Serial.available() > 0) {
    incomingByte = Serial.read();       
    
    
    
    //arduino receives data one byte at a time--we'll need to put data in an array to read through it properly
    if (incomingByte == 'j'){
      Serial.println("kk");
    }
  
  }
}

//yay
//cakebot
//go!!!!!!!!!!!!!!!!!!!!!
