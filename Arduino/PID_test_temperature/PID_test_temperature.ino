const int Capt = A1;
float temperature = 0;

void setup() {
  // put your setup code here, to run once:
     Serial.begin(9600);
     
}

void loop() {
  // put your main code here, to run repeatedly:
  temperature = analogRead(Capt);
  temperature = temperature * (5 / 1023.0 * 100.0) - 273;

  //Serial.println(analogRead(Capt));
  Serial.println(temperature);


  digitalWrite(3, HIGH);
  Serial.println("HAUT");
  delay(3000);
  digitalWrite(3, LOW);
  Serial.println("BAS");
  delay(3000);
}
