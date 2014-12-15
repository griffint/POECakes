//Final Arduino Code for Cakebot
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myExtruder = AFMS.getMotor(1);
Adafruit_DCMotor *myMotor = AFMS.getMotor(2);
Adafruit_StepperMotor *linearMotor = AFMS.getStepper(200,2);

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
int greenInput = 9;



void setup() { 
  AFMS.begin();
  Serial.begin(9600);
  
  //set pinMode for every digital I/O pin
  pinMode(m0Pin,OUTPUT);
  pinMode(m1Pin,OUTPUT);
  pinMode(m2Pin,OUTPUT);
  pinMode(platformLimit1, INPUT);
  pinMode(platformLimit2,INPUT);
  pinMode(topLimit1,INPUT);
  pinMode(topLimit2,INPUT);
  pinMode(platformDir, OUTPUT);
  pinMode(platformStep,OUTPUT);
  pinMode(greenInput,INPUT);
 
 linearMotor->setSpeed(10); 
 myMotor->setSpeed(220);
 myExtruder->setSpeed(220);

}


void loop(){
 //arduino must wait for input before /sending output to python control code
 //always use println

 //need to extract first 3 chars of string to determine code 
 // then create a string out of the rest of the input
 String serials = waitReadSerial();
 delay(100);
 String serialInput = "";  //this is first 3 chars of serial input
 String serialNumbersString = "";   //serialNumbers is the rest of the input code, should always be numbers like steps or time
 
 for (int k=0; k<3; k++){  //needs testing
    char c = serials.charAt(k);
    serialInput += c;
 }

 for (int j=3; j<serials.length(); j++){ //needs testing
    char c = serials.charAt(j);
    serialNumbersString += c;
 }
 
 
 int serialNumbers = serialNumbersString.toInt();
 




 if (serialInput=="CON"){  //connection check
    Serial.println("YES");
 }
 else if (serialInput == "GB?"){ //green button check
    greenButtonCheck();
 }
 else if (serialInput == "OS?"){
 }
 else if (serialInput == "LSI"){
    moveTopStepper(serialNumbers,1);
 }
 else if (serialInput == "LSO"){
    moveTopStepper(serialNumbers,0);
 }
 else if (serialInput == "RPC"){
    spinPlatform(serialNumbers,1);
 }
 else if (serialInput == "RPN"){
    spinPlatform(serialNumbers,0);
 }
 else if (serialInput == "FTD"){
    turnTopFrostingMotor(serialNumbers,1);
 }
 else if (serialInput == "FTU"){
    turnTopFrostingMotor(serialNumbers,0);
 }
 else if (serialInput == "FSD"){
    turnSideFrostingMotor(serialNumbers,1);
 }
 else if (serialInput == "FSU"){
    turnSideFrostingMotor(serialNumbers,0);
 }
 else if (serialInput ==  "CLS"){
   
 }
 else if (serialInput == "CPS"){
   calibratePlatform();
 }



 }
 
 
 //===========END OF MAIN LOOP HERE=================


String waitReadSerial(){
  String readString = "";
   while (!Serial.available()) {} // wait for data to arrive
  // serial read section
  while (Serial.available()>0 ) // this will be skipped if no data present, leading to
                            // the code sitting in the delay function below
  {
    delay(300);  //delay to allow buffer to fill 
    if (Serial.available() >0)
    {
      delay(30);
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
      
    }
  }
  return readString;
}


//=============================================================

void turnTopFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds, input should be in seconds now
//THIS IS VERIFIED WORKING AS OF 8PM SUNDAY NIGHT
   
   int startTime = 0;
   int currentTime = 0;
   startTime=millis();
   
   while((currentTime-startTime)<(time*1000)){
     currentTime = millis();
   
   if (directions==1){
  
       myMotor->run(FORWARD);//backward equates to down
     }
    else{
       myMotor->run(BACKWARD);//backward equates to down
     } 
  }
 myMotor->run(RELEASE);
}

//==========================================================

void turnSideFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds, input should be in seconds
//THIS IS VERIFIED WORKING AS OF 8PM SUNDAY NIGHT
  
   int startTime = 0;
   int currentTime = 0;
   startTime=millis();
   while((currentTime-startTime)<(time*1000)){
   currentTime = millis();
   if (directions==1){
  
     myExtruder->run(FORWARD);//backward equates to down
   }
   else{
     myExtruder->run(BACKWARD);//backward equates to down
   }
 }
 myExtruder->run(RELEASE);
}

//=====================================================

void moveTopStepper(int steps, int directions){  
  //this moves the top frosting motor given # of steps
  //directions should be 1 to move inward, 0 for out
  
  byte spinDir = 0;
  if (directions == 1){
    spinDir = FORWARD;
  }
  else if (directions == 0){
    spinDir = BACKWARD;
  }
  
  linearMotor->step(steps, spinDir,SINGLE); 
 
  linearMotor->release();
}

//==================================================

void calibrateTopStepper(){
  byte val = LOW;
   int counter = 0;
   while (val == LOW && counter<70){
     delay(30);
     spinPlatform(3,1);
     val = digitalRead(topLimit2);  //STILL NEED TO DETERMINE WHICH ONE IS HIGH
     counter = counter+1;
   }
   if (digitalRead(topLimit2==HIGH){
     Serial.println("PSC");
   }
   else {
     Serial.println("no calibratoin");
   }
}

//=======================================================

void greenButtonCheck(){
  byte val = digitalRead(greenInput);
  if (val == HIGH){
    Serial.println("GBP");
  }
  else if (val == LOW){
    Serial.println("GBU");
  }
}

//=====================================================

void calibratePlatform(){
   byte val = LOW;
   int counter = 0;
   while (val == LOW && counter<70){
     delay(30);
     spinPlatform(3,1);
     val = digitalRead(platformLimit2);  //STILL NEED TO DETERMINE WHICH ONE IS HIGH
     counter = counter+1;
   }
   if (digitalRead(platformLimit2==HIGH){
     Serial.println("PSC");
   }
   else {
     Serial.println("no calibratoin");
   }
}

//=====================================================

void spinPlatform(int steps, int directions){  //VERIFIED WORKING, ALTHOUGH SEEMS WEAK
  //this spins the cake platform given # of steps
  //direction of 1 should mean clockwise, 0 = counterclockwise
  //no outputs
 
  int stepCounter = steps;
  digitalWrite(platformDir,LOW);
  if (directions == 1) {  // switches direction if clockwise. May have to change this
    digitalWrite(platformDir,HIGH);
  }

  while (stepCounter>0){
    Serial.println(stepCounter);
    digitalWrite(platformStep, HIGH);
    delay(100);
    digitalWrite(platformStep,LOW);
    stepCounter = stepCounter - 1;
    delay(200);  
 }
}
