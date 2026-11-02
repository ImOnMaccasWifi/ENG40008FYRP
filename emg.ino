int emg_pin = A0;
int emg = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
 

}


void loop() {
  // put your main code here, to run repeatedly:
emg = analogRead(emg_pin);
Serial.println(emg);
delay(100);  

}
