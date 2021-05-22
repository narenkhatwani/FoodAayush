# IoT Device Documentation

### Theory

This code collects value from Gravity PH sensor and send data to flutter app via bluetooth

Hardware: ESP32 Microcontroller, Gravity PH sensor, Push Button, some resistors to make voltage divider circuit

Software: Arduino IDE

PH sensor Calibration: Referred this for calibration 

[Measure pH with a low-cost Arduino pH sensor board](https://www.e-tinkers.com/2019/11/measure-ph-with-a-low-cost-arduino-ph-sensor-board/)

One problem was PH sensor outputs an analog values in range of 0-5V, but ESP32 has ADC of 0-3.3V. So created a voltage divider circuit to reduced output voltage to 3V. 

### Circuit Diagram:

![Imgur Image](https://i.imgur.com/EgfksJK.png)
