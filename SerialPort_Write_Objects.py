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

    __commandList ={0xAAA: "BeginCmd",
                    0xAAB: "EndCmd",
                    0xAAC: "TelemetryCmd"}

    __rwTimeOut = 1

    def __init__(self, _serialClass = serial.Serial(None, 115200) ):
        self._serialClass = _serialClass  #serial port class from PySerial
        self.__writeBuffer = []
        self.__readingBuffer = []

    # print logs function
    def initLog(self):
        print("Passed serial port object: " + str(self._serialClass))

    @property
    def ReadingBuffer(self):
        return self.__readingBuffer
        print("Reading Buffer content: " + str(self.__readingBuffer))

    @ReadingBuffer.getter
    def readingBuffer(self):
        print("Reading Buffer content: " + str(self.__readingBuffer))

    @readingBuffer.setter
    def readingBuffer(self, data):
        self.__readingBuffer.append(data)

    @property
    def WritingBuffer(self):
        return self.__writeBuffer

    @WritingBuffer.getter
    def writingBuffer(self):
        print("Writing Buffer content: " + str(self.__writeBuffer))

    @writingBuffer.setter
    def writingBuffer(self, data):
        self.__writeBuffer.append(data)

    @property
    def getCommandDictionary(self):
        for i, j in self.__commandList.items():
            print("Hex code: {0}, Name: {1}".format(hex(i), j))

    def addCommand(self, newCmdName):
        if type(newCmdName) != str:
            newCmdName = str(newCmdName)
        __newCmdKey = list(self.__commandList.keys())[-1]
        __newCmdKey += 1
        self.__commandList[__newCmdKey] = newCmdName

    def removeCommand(self, cmdName):
        if type(cmdName) != str:
            cmdName = str(cmdName)

        notFoundCounter = 0;
        dictLen = len(self.__commandList)
        for key,val in self.__commandList.items():
            if val == cmdName:
                print("Found command to remove. \nKey: {0}, Name: {1}".format( str(key), str(val)))
                self.__commandList.pop(key)
                break #break loop executing - found command to remove

            notFoundCounter += 1
            if notFoundCounter == (dictLen):
                print("Command to remove not found.")
                break  # break loop - command not found

    @property
    def readWriteTimeOut(self):
        return self.__rwTimeOut

    @readWriteTimeOut.getter
    def readWriteTimeOut(self):
        print("Read/Write time out: " + str(self.__rwTimeOut))

    @readWriteTimeOut.setter
    def readWriteTimeOut(self, timeout):
        try:
            if (timeout < 0):
                raise ValueError
            else:
                self.__rwTimeOut = timeout
        except ValueError:
            print("Invalid time out value. \nValue less than 0!")


arduinoSerialPort = serial.Serial('COM3', 115200)
test_object = SpecSerialPort(arduinoSerialPort)

# test_object.initLog()
# test_object.getReadingBuffer
# test_object.getWritingBuffer
#
# test_object.getCommandDictionary
# test_object.addCommand("GetTemp")
# print("After add new command")
# test_object.getCommandDictionary
# print("After remove")
# test_object.removeCommand("GetTemp")
# test_object.getCommandDictionary
# test_object.ReadWriteTimeOut
# test_object.ReadWriteTimeOut = -100
# test_object.ReadWriteTimeOut

test_object.readingBuffer
test_object.readingBuffer = 10
test_object.readingBuffer

test_object.writingBuffer
test_object.writingBuffer = 100
test_object.writingBuffer