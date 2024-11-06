import serial
import time

ser = serial.Serial('COM3',9600) # open serial port, change to yours!
ser.flushInput()

while True:
    try:
        ser.write('ONE\r\n'.encode())
        print('ONE')
        time.sleep(1)
        ser.write('ZERO\r\n'.encode())
        print('ZERO')
        time.sleep(1)
    except:
        print("Keyboard interrupt")
        break
