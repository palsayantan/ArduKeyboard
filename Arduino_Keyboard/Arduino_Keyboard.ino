#include <Keypad.h>
const byte ROWS = 3; //three rows
const byte COLS = 3; //three columns
//define the cymbols on the buttons of the keypads
char hexaKeys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'}
};
byte rowPins[ROWS] = {10, 9, 8}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {11, 12, 13}; //connect to the column pinouts of the keypad

//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

int LED = 7;

void setup(){
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
}
  
void loop(){
  char customKey = customKeypad.getKey();
  if (customKey){
    Serial.println(customKey);
    digitalWrite(LED,HIGH);
    delay(100);
    digitalWrite(LED,LOW);
  }
}
