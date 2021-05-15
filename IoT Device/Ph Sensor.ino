#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

//Ph sensor 
const int sensorpin = 36;
unsigned long int avgValue;
float b;
const float m = -5.929;
int buf[10], temp;

//Button to active ph sensor
const int wakeuppin = 39;

//Bluetooth
const String BTname = "FoodAyush";
String send_data = "";
int buttonState = 0; 

//Bluetooth serial object
BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin(BTname); //Bluetooth device name
  pinMode(wakeuppin,INPUT);
  //Serial.println("The device started, now you can pair it with bluetooth!");
}

void calph() {
  for (int i = 0; i < 10; i++) {
    temp = analogRead(sensorpin);
    buf[i] = (int)temp;
    delay(10);
  }
  for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 10; j++) {
      if (buf[i] > buf[j]) {
        temp = buf[i];
        buf[i] = buf[j];
        buf[j] = temp;
      }
    }
  }
  avgValue = 0;
  for (int i = 2; i < 8; i++) {
    avgValue += buf[i];
  }
  //Serial.println(avgValue);
  float phValue = (float)avgValue*3.3/4096/6;
  phValue = 7 - (1.42 - phValue) * m;
  Serial.print("pH:");
  //Serial.print(phValue, 2);
  send_data = String(round(phValue));
  Serial.print(send_data);
  SerialBT.println(send_data);
  Serial.println(" ");
  delay(500);
}

void loop(){
  buttonState = digitalRead(wakeuppin);
  if(buttonState == HIGH){
    calph();
    delay(1000);
  }
}
