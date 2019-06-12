int steps_1=2;
int dir_1=3;
int steps_2=38;
int dir_2=36;
int stepTime=10;
int boucles=1000;
int i;

void setup() {
  //We define the different pins that will drive the motors as outputs
  pinMode(steps_1, OUTPUT);
  pinMode(dir_1, OUTPUT);
  pinMode(steps_2, OUTPUT);
  pinMode(dir_2, OUTPUT);
}


void loop() {
  i=0;
  while(i<boucles){//We make the motor go one way
    digitalWrite(dir_1, HIGH);
    digitalWrite(steps_1,HIGH);
    digitalWrite(dir_2, HIGH);
    digitalWrite(steps_2,HIGH);
    delay(stepTime);
  }
  delay(1000);//We take into account the inertia
}
