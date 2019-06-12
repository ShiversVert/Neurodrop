int ledPin = 2;
int i=0;
void setup() {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledPin, HIGH);
  delay(4000);
  Serial.println("LOW");
  digitalWrite(ledPin, LOW);
  delay(4000);
  Serial.println("HIGH");
}
