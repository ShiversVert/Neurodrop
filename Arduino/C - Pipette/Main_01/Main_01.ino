// A simple pipette control sketch.
// For more info visit: http://www.modularscience.com/app/doc/autoPipette
// Use the serial console to send the following commands: up, down


// pin definitions
#define Enter 3
#define Tip 4
#define Plus 5
#define Select 6
#define Moins 7
#define Start 8


// info about the current incoming command
#define MAX_COMMAND_LEN 5
char command[ MAX_COMMAND_LEN + 1 ]; // leave room for zero terminator
int commandPos = 0;
boolean commandDone = false;


// run once on startup: set up serial and output pins
void setup() {
  Serial.begin( 9600 );
  pinMode( Tip, OUTPUT );
  digitalWrite( Tip, LOW );

  pinMode( Enter, OUTPUT );
  digitalWrite( Enter, LOW );

  triggerButton( Tip );
  Serial.println("init");
  delay(14000);
}

void loop() {
  triggerButton(Enter);
  Serial.println("Center_PIN triggered");
  
  delay(5000); 
}


// trigger a button using a relay
void triggerButton( int pin ) {
  digitalWrite( pin, HIGH );
  delay(100);
  digitalWrite( pin, LOW ); 
}
