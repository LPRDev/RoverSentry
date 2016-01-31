/*
* ArduTest.ino
* Version:   1.1
* Author:    Peter Reinert
*/

byte ledPin = 13;
byte input=0;

/*
* Setup()
* baud rate must be the same as serial_request.py
*/
void setup() {
  Serial.begin(115200);  
  pinMode(ledPin, OUTPUT);
}

/*
* loop()
* wait for data in buffer and respond accordingly
*/
void loop() {
  input=' ';
  if (Serial.available()>0) {
    input = Serial.read();
    switch(input) { // input must be single character
      case '0':
        Serial.write("Paused");
        blink_led();  // one blink indicates pause
        delay(1000);
        break;
      case '1':
        Serial.write("Resuming");
        blink_led(); // two blinks indicate resume
        blink_led();
        delay(1000); 
        break;
      default:  ;
    }
  }
}

/*
* blink_led()
* will blink the board led one time
*/
void blink_led()
{
  for (int i=1; i<2; i++){
  digitalWrite(ledPin, HIGH); // turn ON LED
  delay(150);  // Just wait 1s
  digitalWrite(ledPin, LOW); //  switch OFF
  delay(150); 
  }
}
