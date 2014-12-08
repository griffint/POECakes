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


}


void loop(){
 //arduino must wait for input before sending output to python control code
 //always use println
 
 String serialInput = waitReadSerial();
  
 if (serialInput == "CON"){
   Serial.println("YES");
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
  
}

void turnSideFrostingMotor(int time, int directions){  //this turns the extruding motor a given milliseconds
  
}

void moveTopStepper(int steps, int directions){ //this moves the top frosting motor given # of steps
  
}

void spinPlatform(int steps, int directions){ //this spins the cake platform given # of steps

}
