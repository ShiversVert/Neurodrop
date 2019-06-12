int sensorPin = 0;
int ledPin = 2;
int val = 0;
 
void setup() {
    Serial.begin(9600);
    pinMode(sensorPin,INPUT);
    pinMode(2,OUTPUT);
}
 
void loop() {
    val = analogRead(sensorPin);
    Serial.println(val);
    
    if(val>200){
      digitalWrite(ledPin,HIGH);
    }
    delay(10);
    digitalWrite(ledPin, LOW);
}
