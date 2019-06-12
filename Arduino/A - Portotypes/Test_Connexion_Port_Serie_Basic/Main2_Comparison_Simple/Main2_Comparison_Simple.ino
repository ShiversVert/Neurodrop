int entree = 0;
int sortie = 1;
int in = 0;
int out = 0;
int res = 0;
 
void setup() {
    Serial.begin(9600);
    pinMode(entree,INPUT);
    pinMode(sortie,INPUT);
}
 
void loop() {
    in = analogRead(entree);
    out = analogRead(sortie);
    Serial.println(String(in)+";"+String(out));
    
    delay(100);
}
