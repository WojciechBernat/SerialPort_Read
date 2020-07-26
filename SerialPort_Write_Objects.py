import time
import serial
from DetectSerialPort import DetectSerialPort



arduinoSerialPort = serial.Serial('COM3', 115200)
from SpecialSerialPort import SpecialSerialPort
test_object = SpecialSerialPort(arduinoSerialPort)

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
#
# test_object.readingBuffer
# test_object.readingBuffer = 10
# test_object.readingBuffer
#
# test_object.writingBuffer
# test_object.writingBuffer = 100
# test_object.writingBuffer

# test_object.commandDictionary
# test_object.commandDictionary = "GetTemp"
# test_object.commandDictionary
# test_object.removeCommand("GetTemp")
# test_object.commandDictionary


