//Digital Pins
int PinDirVert = 22;
int PinDirHor = 23;
int PinEWOD1 = 24;
int PinEWOD2 = 25;
int PinEWOD3 = 26;
int PinEWOD4 = 27;
int PinEWOD5 = 28;

//Digital PWM pins
int PinStepVert = 2;
int PinStepHor = 3;

//Analog Pins
int PinSiPM = 0

//Variables
int val=0;
int measure=0;
int i=0;
int j=0;

void setup() {
  Serial.begin(9600);//Initialisation of serial port
  //Definition of the actuator pins
  pinMode(PinDirVert,OUTPUT);
  pinMode(PinDirHor,OUTPUT);
  pinMode(PinEWOD1,OUTPUT);
  pinMode(PinEWOD2,OUTPUT);
  pinMode(PinEWOD3,OUTPUT);
  pinMode(PinEWOD4,OUTPUT);
  pinMode(PinStepVert,OUTPUT);
  pinMode(PinStepHor,OUTPUT);
  //Definition of the input pins
  pinMode(PinSiPM,INPUT);
}

void loop() {
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

int MoveToPosition(int pad_number_now,int pad_number_obj){
  y_now=pad_number_now%4;//If we have 2^4 pads
  x_now=pad_number_obj-4*y_now;
  y_obj=pad_number_now%4;//If we have 2^4 pads
  x_obj=pad_number_obj-4*y_obj;
  
}
