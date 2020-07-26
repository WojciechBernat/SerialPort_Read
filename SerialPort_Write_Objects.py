import time
import serial
from DetectSerialPort import DetectSerialPort



arduinoSerialPort = serial.Serial('COM3', 115200)
from SpecialSerialPort import SpecialSerialPort
test_object = SpecialSerialPort(arduinoSerialPort)


test_object.comDetect.toFind = 'Arduino'
test_object.comDetect.toFind
test_object.comDetect.detectPort()

test_object.readingBuffer = '2766\n'
test_object.readingBuffer

test_object.comLayer.writeFromBuffer()
# time.sleep(test_object.readWriteTimeOut)
# test_object.comLayer.readToBuffer()


