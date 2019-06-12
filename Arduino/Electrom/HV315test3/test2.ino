// on définit la constante en donnant un nom et un nombre.
const int start = 2;
const int fin = 7;
bool val;

void setup(){
  // on l'utilise en écrivant juste son nom
  for (int i = start; i <= fin; i++) {
    pinMode(i, OUTPUT);
  }
  setAllLed(LOW, start, fin);delay(75);
  setAllLed(HIGH, start, fin);delay(75);
  setAllLed(LOW, start, fin);delay(75);
  setAllLed(HIGH, start, fin);delay(75);
  setAllLed(LOW, start, fin);delay(75);
  setAllLed(HIGH, start, fin);delay(75);
  setAllLed(LOW, start, fin);delay(75);
  setAllLed(HIGH, start, fin);delay(75);
  setAllLed(LOW, start, fin);delay(75);
  
}
void loop(){
  for (int i = 2; i <= 7; i+=1) {
    int next = i+1;
    if (i >= 7){
      next = 2;
    }
    //blinkLedOnce(i, 3000);
    blinkTowLedOnce(i, next, 2000);
  }
}


void blinkTowLedOnce(int id1, int id2, int duration) {
  digitalWrite(id1, HIGH);
  digitalWrite(id2, HIGH);
  delay(duration);
  digitalWrite(id1, LOW);
  digitalWrite(id2, LOW);
}

void blinkLedOnce(int id, int duration) {
  digitalWrite(id, HIGH);
  delay(duration);
  digitalWrite(id, LOW);
}

void setAllLed(bool value, int start, int fin) {
  for (int i = start; i <= fin; i++) {
    digitalWrite(i, value);
  }
}
