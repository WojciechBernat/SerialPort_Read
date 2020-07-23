import time
import serial
#import serial.tools.list_ports

#special class for serial port
class SpecSerialPort:
    #constructor - init pyserial class
    # default:
    # port: None
    # baudrate = 115200
    # the rest by default

    _commandList ={0xAAA: "BeginCmd",
                  0xAAB: "EndCmd",
                  0xAAC: "TelemetryCmd"}

    def __init__(self, _serialClass = serial.Serial(None, 115200) ):
        self._serialClass = _serialClass  #serial port class from PySerial
        self._writeBuffer = []
        self._readingBuffer = []

    # print logs function
    def initLog(self):
        print("Passed serial port object: " + str(self._serialClass))

    def printReadingBuffer(self):
        print("Reading Buffer content: " + str(self._readingBuffer))

    def printWritingBuffer(self):
        print("Writing Buffer content: " + str(self._writeBuffer))

    def printCommandDictionary(self):
        for i, j in self._commandList.items():
            print("Hex code: {0}, Name: {1}".format( hex(i), j))


arduinoSerialPort = serial.Serial('COM3', 115200)
test_object = SpecSerialPort(arduinoSerialPort)

# print("Serial port class" + str(arduinoSerialPort))
# print("General serial port object: " + str(test_object))

test_object.initLog()
test_object.printReadingBuffer()
test_object.printWritingBuffer()
test_object.printCommandDictionary()