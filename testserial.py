import serial #Serial imported for Serial communication
import time #Required to use delay functions

ser = serial.Serial('/dev/cu.usbserial-1140',9600)
connected = False
time.sleep(2)
while not connected:
    serin = ser.read()
    connected = True

ser.write("1")

while ser.read() == '1':
    print(ser.read())
