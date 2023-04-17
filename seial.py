import serial #Serial imported for Serial communication
import time #Required to use delay functions

ArduinoSerial = serial.Serial('/dev/cu.usbserial-1110',9600)

time.sleep(2)

def open():

    text = '0'
    ArduinoSerial.write((bytes(text, 'utf-8')))


def close():
    text = '1'
    ArduinoSerial.write((bytes(text, 'utf-8')))
    






