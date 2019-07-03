#include <MultiStepper.h>
#include <AccelStepper.h>

int i=0;
int var0=0;
int var1=0;
int var2=0;
int var3=0;
int var4=0;
int var5=0;

String lect;

AccelStepper motorX = AccelStepper(1, 13, 12);
AccelStepper motorZ = AccelStepper(1, 11, 10);

void setup() {
  // put your setup code here, to run once:
  motorX.setMaxSpeed(50000);
  motorX.setAcceleration(1000);
  motorZ.setMaxSpeed(50000);
  motorZ.setAcceleration(1000);
  Serial.begin(9600);
  for(i=2;i<14;i++){
    pinMode(i,OUTPUT);
  }
  pinMode(A0,INPUT);
  Serial.println("Arduino OK");
}

void loop() {
  var0=read_serial(var0); //We read the first type of command
  if(var0>0){
    switch(var0){
      case 1: // We want to set a button to a certain value
        var1=read_serial(var1); //We get the desired state of the pin
        var2=read_serial(var2); //We get the pin of the pin
        switch(var1){
          case 0: // We want to put the pin to the LOW state
            digitalWrite(var2,LOW);
            break;

          case 1: // We want to put the pin to the HIGH state
            digitalWrite(var2,HIGH);
            break;

          default:
            break;
        }
        break;

      case 2: // We want to create a step signal
        var1=read_serial(var1); // We get the number of steps, the pin and the first state
        var4=var1%10; // We extract the first state
        var1=(var1-var4)/10;
        var2=var1%100;// We extract the pin that has to be activated
        var1=(var1-var2)/100;// We extract the number of steps
        var3=read_serial(var3); // We get the half period of the steps
        switch(var4){
          case 0:
            for(i=0;i<var1;i++){
              digitalWrite(var2,LOW);
              delay(var3);
              digitalWrite(var2,HIGH);
              delay(var3);
            }
            break;
            
          case 1:
            for(i=0;i<var1;i++){
              digitalWrite(var2,HIGH);
              delay(var3);
              digitalWrite(var2,LOW);
              delay(var3);
            }
            break;

          default:
            break;
        }
        break;

        case 3: // We activate a motor
          var1=read_serial(var1); // We get the first position of the motor and the motor to activate
          var3=var1%10; // We extract the number of the motor to activate
          var1=(var1-var4)/10;
          var2=read_serial(var2); // We get the final position of the motor
          switch(var3){
            case 0:
              motorX.setCurrentPosition(var1);
              motorX.moveTo(var2);
              motorX.runToPosition();
              break;

            case 1:
              motorZ.setCurrentPosition(var1);
              motorZ.moveTo(var2);
              motorZ.runToPosition();
              break;
          }
          break;

        case 4: // We create a PWM
          var1=read_serial(var1); // We get the number of the pin we want to set the PWM 
          var2=read_serial(var2); // We get the value of the PWM
          analogWrite(var1,var2);
          break;

        case 5: // We do a series of measurements
          var1=read_serial(var1); // We get the pin we want to read
          var2=read_serial(var2); // We get the number of measures we have to do
          var3=read_serial(var3); // We get the time between measures
          for(i=0;i<var2;i++){
            var4=analogRead(var1);
            Serial.println(var4);
            delay(var3);
          }
        break;
        
      default:
        break;
    }
  }
}

int read_serial(int num){
    /* This function reads the serial port, sends the confirmation message, and returns the value as an int*/
    while (not(Serial.available())){
        delay(10);
    }
    String lect=Serial.readStringUntil('\n'); 
    var5=lect.length();
    num=0;
    for(i=0; i<var5; i++){
        num = num * 10 + ( lect[i] - '0' );
    }
    Serial.println("ACK "+lect);
    return num;
}
