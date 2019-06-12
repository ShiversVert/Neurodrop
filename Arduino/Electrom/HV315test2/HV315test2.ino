const int _BL = 32;
const int _POL = 30;
const int _LE = 28;
const int _SHORT = 26;
const int _HiZ = 24;
const int GND = 22;
const int CLK = 52;
const int DIN = 51;
const int period = 10;

bool state;
bool polState;
int count;
int data;

void setup() {
  Serial.begin(9600);
  count = 0;

  pinMode(GND, OUTPUT);
  pinMode(_BL, OUTPUT);
  pinMode(_POL, OUTPUT);
  pinMode(_HiZ, OUTPUT);
  pinMode(_LE, OUTPUT) ;
  pinMode(CLK, OUTPUT) ;
  pinMode(DIN, OUTPUT) ;
  pinMode(_SHORT, INPUT);

  // Initialisation
  digitalWrite(GND, LOW);
  digitalWrite(_BL, LOW);
  digitalWrite(_POL, LOW);
  digitalWrite(_HiZ, HIGH);
  digitalWrite(_LE, LOW) ;
  digitalWrite(CLK, LOW) ;
  digitalWrite(DIN, LOW) ;
}

void loop() {
  count++;
  state = not(state);
  digitalWrite(CLK, state) ;
  if(count = 100){
    polState = not(polState);
    Serial.println(polState);
    digitalWrite(_POL, polState);
    count = 0;  
  }
  delay(period);
}
