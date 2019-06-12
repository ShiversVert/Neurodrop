int PinLed = 2;
int PinPhototransistor = 1;
int PinVerifLed = 0;
int val=0;
int measure=0;
int i=0;
int j=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PinLed,OUTPUT);
  pinMode(PinPhototransistor, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  i=0;
  while(i<255){
    j=0;
    analogWrite(PinLed,i);
    while(j<10){
      measure=analogRead(PinPhototransistor);
      Serial.println(String(i)+';'+String(measure));
      j=j+10;
      delay(1);
    }
    i=i+1;
  }
}
