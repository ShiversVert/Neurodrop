int PinLed = 0;
int PinPhototransistor = 1;
int val=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PinLed,OUTPUT);
  pinMode(PinPhototransistor, INPUT);
  Serial.println("=======START======");
}

void loop() {
  // put your main code here, to run repeatedly:
  i=0;
  while(i<255){
    j=0;
    analogWrite(PinLed,i);
    while(j<1000){
      val=analogRead(PinPhototransistor);
      Serial.println(val);
      j=j+1;
      delay(10);
    }
    i=i+17;
  }
}
