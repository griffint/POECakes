void setup() { 
  
  Serial.begin(9600);

}


void loop(){
  
   String serials = waitReadSerial();
   //Serial.println("Out of serial reading");
   //Serial.println(serials);
 String serialInput = "";
 String serialNumbers = "";  
  
   for (int i=0; i<3; i++){  //needs testing
    char c = serials.charAt(i);
    serialInput += c;
 }
 
 if (serialInput=="CON"){
   //Serial.println("YES");
 }
 //Serial.println(serialInput);

 for (int j=3; j<(serials.length()); j++){ //needs testing
    char c = serials.charAt(j);
    serialNumbers += c;
 }
 
 //Serial.println(serialNumbers);
 
}



String waitReadSerial(){
  //Serial.println("wait Serial is running");
   while (!Serial.available()) {} // wait for data to arrive
  // serial read section
  int serialCounter = Serial.available();
  String readString;
  while (Serial.available()>0) // this will be skipped if no data present, leading to
                            // the code sitting in the delay function below
  {
    delay(100);  //delay to allow buffer to fill 
    //Serial.println(Serial.available()); 
    
    
    
    if (Serial.available() >0)
    {
      delay(30);
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
      //Serial.println("The readString is");
      //Serial.print(readString);
      
    }
  }
  return readString;
}
