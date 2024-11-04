// Reading data from Serial port 
// and print it to LCD screen
// by Judhi P. 2022

#include <Wire.h>  // necessary for using LCD
#include <LiquidCrystal_I2C.h>  // LiquidCrystal i2c by Frank de Brabander
LiquidCrystal_I2C lcd(0x27, 16, 2);  // select LCD at i2c address 0x27
String data;    // variable to receive data from serial port

void setup()
{
  lcd.init();  // initializing LCD
  lcd.backlight();  // turn on the backlight
  lcd.clear();  // clear LCD screen
  lcd.print("Ready!");
  Serial.begin(9600);  // start serial communication at 9600 baud
}
void loop()
{
  while(Serial.available()) {  // checking serial port
    data = Serial.readString();  // reading data
    data.trim();  // remove white spaces and non-printable characters
    lcd.clear();  // clear LCD screen
    lcd.print(data);  // print data on LCD
  }
}
