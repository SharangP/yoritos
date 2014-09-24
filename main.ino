/**************************
 * Yo enabled vending machine
 *************************>

#define BUTTON_PRESS_TIME 500

//Arduino pins corresponding to vending machine numbers [0, 1, ...9]
const int pins[9] = {2, 3, 4, 5, 6, 7, 8, 9, 10};

void pressNumber(const int number) {
  digitalWrite(pins[number], HIGH);
  delay(BUTTON_PRESS_TIME);
  digitalWrite(pins[number], LOW);
}

void setup() {
  Serial.begin(9600);
    for (int i = 0; i < sizeof(pins)/sizeof(int); i++) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}

void loop() {
  if(Serial.available() > 0) {
    int incomingByte = Serial.read();
    Serial.println(incomingByte, DEC);
    //TODO: press each decimal digit of the int(incomingByte)
  }
  delay(1000);
}
