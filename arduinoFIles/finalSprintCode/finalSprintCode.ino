//Final Arduino Code for Cakebot
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *myExtruder = AFMS.getMotor(4);
Adafruit_DCMotor *myMotor = AFMS.getMotor(3);
Adafruit_StepperMotor *linearMotor = AFMS.getStepper(200,1);

//code here to initialize all digital input ports


void setup() { 
  AFMS.begin();
  myMotor->setSpeed(250);
  linearMotor->setSpeed(30);
  Serial.begin(9600);

}


void loop(){
 //arduino must wait for input before sending output to python control code
 //always use println
 
 //need to extract first 3 chars of string to determine code 
 // then create a string out of the rest of the input
 String serials = waitReadSerial();
 String serialInput = "";
 String serialNumbers = "";   //serialNumbers is the rest of the input code, should always be numbers like steps or time
 
 for (int i=0, i<3, i++){  //needs testing
    char c = serials.charAt(i);
    serialInput += c;
 }

 for (int j=3, i<string.length(serials), i++){ //needs testing
    char c = serials.charAt(j);
    serialNumbers += c;
 }

  
 if (serialInput == "CON"){
   Serial.println("YES");
 }
 if (serialInput == "TLS"){
   moveTopStepper();
 }
 
 if (serialInput == "TRP"){
   spinPlatform();
 }
 
 if (serialInput == "TFT"){
   turnTopFrostingMotor();
 }
 
 if (serialInput == "TFS"){
   turnSideFrostingMotor();
 }
 
 if (serialInput == "LSI"){
   directions = 1;
   moveTopStepper();
 }
 
 if (serialInput == "LSO"){
   directions = 0;
   moveTopStepper();
 }
 
 if (serialInput == "FTD"){
   directions = 1;
   turnTopFrostingMotor();
}
 
 if (serialInput = "FTU"){
   directions = 0;
   turnTopFrostingMotor();
 } 
 
  if (serialInput == "FSD"){
   directions = 1;
   turnSideFrostingMotor();
}
 
 if (serialInput = "FSU"){
   directions = 0;
   turnSideFrostingMotor();
 }
 
 if (serialInput == "RPC"){
   directions = 1;
   spinPlatform();
}
 
 if (serialInput = "FSU"){
   directions = 0;
   spinPlatform();
 }
 
 
 
 }


String waitReadSerial(){
   while (!Serial.available()) {} // wait for data to arrive
  // serial read section
  while (Serial.available()) // this will be skipped if no data present, leading to
                             // the code sitting in the delay function below
  {
    delay(30);  //delay to allow buffer to fill 
    if (Serial.available() >0)
    {
      String readString;
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }
}

void turnTopFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds
   myMotor->setSpeed(220);
   int startTime = 0;
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

void turnSideFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds
  myExtruder->setSpeed(220);
   int startTime = 0;
   int currentTime = 0;
   startTime=millis();
   int k = 0;
   while(k<9){//this should check for time being passed instead of k, get rid of k
   
   if (directions==1){
  
   myExtruder->run(FORWARD);//backward equates to down
 }
 else{
   myExtruder->run(BACKWARD);//backward equates to down
 }
   int currentTime = millis();
   delay(500);
   Serial.print("in loop");
   
   k+=1;
 }
 myExtruder->run(RELEASE);
}

void moveTopStepper(int steps, int directions){ //this moves the top frosting motor given # of steps
  linearMotor->setSpeed(220);
   int startTime = 0;
   int currentTime = 0;
   startTime=millis();
   int k = 0;
   while(k<9){
   
   if (directions==1){
  
   linearMotor->run(FORWARD);//backward equates to in
 }
 else{
   linearMotor->run(BACKWARD);//backward equates to out
 }
   int currentTime = millis();
   delay(500);
   Serial.print("in loop");
   
   k+=1;
 }
  linearMotor->run(RELEASE);
}

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
      linearMotor->step(0, FORWARD, MICROSTEP);
      Serial.println("Released"); }

    
  if (reading == HIGH) {
    Serial.println("System OFF");}
}}
}

void spinPlatform(int steps, int directions){ //this spins the cake platform given # of steps
  int stepCounter = steps;
  while (stepCounter>0){
    Serial.print("turn a step");
    digitalWrite(platformStep, HIGH);
    delay(200);
    digitalWrite(platformStep,LOW);
    stepCounter -= 1;
    delay(200);
  
  while (stepCounter<0){
    Serial.print(
  
}}
