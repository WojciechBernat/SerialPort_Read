import time
import serial

arduinoSerialPortBuffer = []
arduinoBeginCmd = b'2766\r\n'


##Init
arduinoSerialPort = serial.Serial('COM3', 115200)
