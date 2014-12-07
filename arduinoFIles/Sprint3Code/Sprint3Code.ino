//POE CakeBot Team Code
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
<<<<<<< Updated upstream
Adafruit_DCMotor *myMotor = AFMS.getMotor(3);
Adafruit_StepperMotor *linearMotor = AFMS.getStepper(200,1);
=======
Adafruit_DCMotor *myMotor = AFMS.getMotor(1);
Adafruit_StepperMotor *myMotorTwo = AFMS.getStepper(200, 2);

>>>>>>> Stashed changes
//code for motor shield stepper motor here

//also need code to initialize input ports for switches

const int limitOne = 9;
const int limitTwo = 8;
const int masterOnOff = 4;

void setup() {
  AFMS.begin();
  myMotor->setSpeed(250);
  linearMotor->setSpeed(30);
  Serial.begin(9600);
  
   pinMode (limitOne, INPUT);
   pinMode (limitTwo, INPUT);
   pinMode (masterOnOff, INPUT);
}


void loop() {
<<<<<<< Updated upstream
  Serial.print("Starting");
//  turnFrostingMotor(200,0);
//  Serial.print("Delay time");
//  delay(1000);
  int i=0;
  
  turnPlatform(20,0);
  delay(5000);
  
  
  //turnFrostingMotor(200,0);
  //Serial.print("Delay time");
  //delay(1000);
  //delay(500);
 
//  delay(500);
//  turnFrostingMotor(200,1);
//  Serial.print("Delay time");
//  delay(1000);
//  i+=1;
//  Serial.print(i);
  
=======
>>>>>>> Stashed changes
  
  //motor check code
  
  //button press code here
  
  //printing design code here 
  
}

void turnFrostingMotor(int time, int directions){
 //this will turn the frosting motor for a given time
 //directions will be 0 or 1
 myMotor->setSpeed(220);
 int startTime=0;
 int currentTime = 0;
 startTime=millis();
 int k = 0;
 while(k<9){
   
   if (directions==1){
  
   myMotor->run(FORWARD);//backward equates to down
 }
 else{
   myMotor->run(BACKWARD);//backward equates to down
 }
   int currentTime = millis();
   delay(500);
   Serial.print("in loop");
   
   k+=1;
 }
 myMotor->run(RELEASE);
}


void turnlinearStepper(int steps, int directions){
  //this will turn the linear actuation motor the given number of steps
  //directions will be 0 or 1
  //this motor will use the adafruit library
  
} 

int limitSwitchOne() {
  int reading = digitalRead(masterOnOff);
  int callibrateOne = digitalRead(limitOne);
  int callibrateTwo = digitalRead(limitTwo);
    
 if (reading == LOW) { 
  //Serial.println("System ON");
  if (callibrateOne == LOW) { // START ROTATING
     // myMotor->step(1, FORWARD, MICROSTEP);
      Serial.println("Pressed");
    }
     if (callibrateTwo == LOW) { // ALL FLASHING
      myMotorTwo->step(0, FORWARD, MICROSTEP);
      Serial.println("Released"); }

    
  if (reading == HIGH) {
    Serial.println("System OFF");}
}}

//=============this guy will turn a step command into the commands the stepper motor===
//=================connected to the platform motor needs=================
void turnPlatform(int steps, int directions){
  //directions will be 0 or 1
  //this motor will use the pololu driver, so will need to use individual steps
<<<<<<< Updated upstream
  //pin 7 for step 8 for direction
 int stepCounter = steps;
  while (stepCounter>0){
    Serial.print("turn a step");
    digitalWrite(platformStep, HIGH);
    delay(200);
    digitalWrite(platformStep,LOW);
    stepCounter -= 1;
    delay(200);
  }
=======
  
>>>>>>> Stashed changes
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
