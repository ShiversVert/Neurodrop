#include <SPI.h>

//const byte Pad[8] = {B00000001, B00000010, B00000100, B00001000, B00010000, B00100000, B01000000, B10000000};
const int Pad[8] = {B11111110, B11111101, B11111011, B11110111, B11101111, B11011111, B10111111, B01111111};

const int _BL = 32;
const int _POL = 30;
const int _LE = 28;
const int _SHORT = 26;
const int _HiZ = 24;
const int GND = 22;

byte data;

void setup()
{
   Serial.begin(9600);
   SPI.begin();
   SPI.setBitOrder(MSBFIRST);
   SPI.setClockDivider(SPI_CLOCK_DIV2);
   
   digitalWrite(GND, LOW);
   digitalWrite(_BL, LOW);
   digitalWrite(_HiZ, HIGH);
   digitalWrite(_LE, LOW) ;
   digitalWrite(_POL, HIGH);
  digitalWrite(_BL, HIGH);
   
   Serial.println("CHECK TENSION AND PRESS A KEY");
   delay(5000);
   /*
   while(!Serial.available() ){
    Serial.read();
   }*/
   Serial.println("INITIALISATION DONE");
   
}

void loop()
{
   for(int i = 0;  i <= 7; i++){
      SPI.transfer(Pad[i]);
      Serial.println(i);
      
      delay(2000);
   }
   
}
