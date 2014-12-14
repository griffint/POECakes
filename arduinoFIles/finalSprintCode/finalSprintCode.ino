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
  
  Serial.begin(9600);

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
   step = 5;
   spinPlatform();
}
 
 if (serialInput == "RPN"){
   step = -5;
   spinPlatform();
 }
 
 if (serialInput == "CLS"){
   calibrateLinear();
 }
 
 if (serialInput == "CPS"){
   calibrateStepper();
 }
 


 if (serialInput == "GB?"){
   drawingButton();
 }
 
 if (serialInput == "OS?"){
   callibrateLinear();
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
  
  
 
  linearMotor->run(RELEASE);
}



void calibrateLinear(int steps, int directions){
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


void drawingButton(int steps, int directions){
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



void spinPlatform(int steps, int directions){ //this spins the cake platform given # of steps
  int stepCounter = steps;
  //int turn = directions;
  while (stepCounter>0){
    Serial.print("turn a step cw");
    digitalWrite(platformStep, HIGH);
    delay(200);
    digitalWrite(platformStep,LOW);
    stepCounter -= 1;
    delay(200);
  
  while (stepCounter<0){
    Serial.print("turn a step ccw");
    digitalWrite(platformStep, LOW);
    delay(200);
    digitalWrite(platformStep, HIGH);
    stepCounter -= 1;
    delay(200); }
  
}
