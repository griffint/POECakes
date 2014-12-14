//Final Arduino Code for Cakebot
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myExtruder = AFMS.getMotor(4);
Adafruit_DCMotor *myMotor = AFMS.getMotor(3);
Adafruit_StepperMotor *linearMotor = AFMS.getStepper(200,1);

//code here to initialize all digital I/O ports as ints

int m0Pin = 0;
int m1Pin = 1;
int m2Pin = 2;
int platformLimit1 = 3;
int platformLimit2 = 4;
int topLimit1 = 5;
int topLimit2 = 6;
int platformDir = 7;
int platformStep = 8;
int 


void setup() { 
  AFMS.begin();
  Serial.begin(9600);
  
  //set pinMode for every digital I/O pin
  pinMode(platformLimit, INPUT);
  pinMode(platformDirection, OUTPUT)
  
}


void loop(){
 //arduino must wait for input before sending output to python control code
 //always use println
 
 //need to extract first 3 chars of string to determine code 
 // then create a string out of the rest of the input
 String serials = waitReadSerial();
 String serialInput = "";  //this is first 3 chars of serial input
 String serialNumbers = "";   //serialNumbers is the rest of the input code, should always be numbers like steps or time
 
 for (int i=0, i<3, i++){  //needs testing
    char c = serials.charAt(i);
    serialInput += c;
 }

 for (int j=3, i<string.length(serials), i++){ //needs testing
    char c = serials.charAt(j);
    serialNumbers += c;
 }

switch (serialInput) {
  case "CON":  //connection check
    Serial.println("YES");
    break;
  case "GB?": //green button check
    break;
  case "OS?":
    break;
  case "LSI":
    moveTopStepper(serialNumbers,1);
    break;
  case "LSO":
    moveTopStepper(serialNumbers,0);
    break;
  case "RPC":
    spinPlatform(serialNumbers,1);
    break;
  case "RPN":
    spinPlatform(serialNumbers,0);
    break;
  case "FTD":
    turnTopFrostingMotor(serialNumbers,1);
    break;
  case "FTU":
    turnTopFrostingMotor(serialNumbers,0);
    break;
  case "FSD":
    turnSideFrostingMotor(serialNumbers,1);
    break;
  case "FSU":
    turnSideFrostingMotor(serialNumbers,0);
    break;
  case "CLS":
    break;
  case "CPS":
    break;
}


 }
 
 
 //===========END OF MAIN LOOP HERE=================


String waitReadSerial(){
  
   while (!Serial.available()) {} // wait for data to arrive
  // serial read section
  while (Serial.available()) // this will be skipped if no data present, leading to
                            // the code sitting in the delay function below
  {
    delay(80);  //delay to allow buffer to fill 
    if (Serial.available() >0)
    {
      String readString;
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
      
    }
  }
  return readString;
}




void turnTopFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds
   myMotor->setSpeed(220);
   int startTime = 0;
   int currentTime = 0;
   startTime=millis();
   
   while((currentTime-startTime)<time){
   
   if (directions==1){
  
       myMotor->run(FORWARD);//backward equates to down
     }
    else{
       myMotor->run(BACKWARD);//backward equates to down
     }
   int currentTime = millis();
   
  }
 myMotor->run(RELEASE);
}



void turnSideFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds
  myExtruder->setSpeed(220);
   int startTime = 0;
   int currentTime = 0;
   startTime=millis();
   while((currentTime-startTime)<time){
   
   if (directions==1){
  
     myExtruder->run(FORWARD);//backward equates to down
   }
   else{
     myExtruder->run(BACKWARD);//backward equates to down
   }
   int currentTime = millis();
   
 }
 myExtruder->run(RELEASE);
}


void moveTopStepper(int steps, int directions){ 
  //this moves the top frosting motor given # of steps
  //directions should be 1 to move inward, 0 for out
  linearMotor->setSpeed(60);
  byte spinDir = 0;
  if (directions == 1){
    spinDir = FORWARD;
  }
  else if (directions == 0){
    spinDir = BACKWARD;
  }
  linearMotor.step(steps, spinDir,SINGLE) 
 
  linearMotor.release();
}



void calibrateTopStepper(){
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
      linearMotor->step(0, FORWARD, MICROSTEP);
      Serial.println("Released"); }

    
  if (reading == HIGH) {
    Serial.println("System OFF");}
}}
}


void greenButton(int steps, int directions){
  int exportButton() {
  int greenReading = digitalRead(greenButton);
  int orangeReading = digitalRead(masterOnOff);
    
 if (orangeReading == LOW) { 
  //Serial.println("System ON");
  if (greenReading == LOW) { // START ROTATING
     linearMotor->step(0, FORWARD, MICROSTEP);
      Serial.println("Set Go");
    }
 
  if (greenReading == HIGH) {
    Serial.println("Paused");}
}}

}


void calibrateStepper(int steps, int directions){
  int limitSwitchOne() {
  int reading = digitalRead(masterOnOff);
  int callibrateOne = digitalRead(limitOne);
  int callibrateTwo = digitalRead(limitTwo);
    
 if (reading == LOW) { 
  //Serial.println("System ON");
  if (callibrateOne == LOW) { // START ROTATING
      //digitalWrite(platformStep, HIGH);
      Serial.println("Pressed");
    }
     if (callibrateTwo == LOW) {
      digitalWrite(platformStep, LOW);
      Serial.println("Released"); }}

    
  if (reading == HIGH) {
    Serial.println("System OFF");}
 }
}



void spinPlatform(int steps, int directions){ 
  //this spins the cake platform given # of steps
  //direction of 1 should mean clockwise, 0 = counterclockwise
  //no outputs
  int stepCounter = steps;
  digitalWrite(platformDirection,LOW)
  if (directions == 1) {  // switches direction if clockwise. May have to change this
    digitalWrite(platformDirection,HIGH)
  }

  while (stepCounter>0){
    digitalWrite(platformStep, HIGH);
    delay(100);
    digitalWrite(platformStep,LOW);
    stepCounter -= 1;
    delay(200);  
}
