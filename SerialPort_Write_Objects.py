import time
import serial
#import serial.tools.list_ports


class serialPort:
    #constructor - init pyserial class
    # default:
    # port: None
    # baudrate = 115200
    # the rest by default
    def __init__(self, _serialClass = serial.Serial(None, 115200) ):
        self._serialClass = _serialClass  #serial port class from PySerial

    # print logs function
    def initLog(self):
        print("Passed serial port object: " + str(self._serialClass))


arduinoSerialPort = serial.Serial('COM3', 115200)
print("Serial port class" + str(arduinoSerialPort))
test_object = serialPort(arduinoSerialPort)

print("General serial port object: " + str(test_object))
test_object.initLog()