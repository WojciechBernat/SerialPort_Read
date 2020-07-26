import time
import serial
from DetectSerialPort import DetectSerialPort



arduinoSerialPort = serial.Serial('COM3', 115200, timeout=0.2, write_timeout=0.2)
from SpecialSerialPort import SpecialSerialPort
test_object = SpecialSerialPort(arduinoSerialPort)

test_object.commandDictionary
print(test_object.getCommandKey("EndCmd"))

# test_object.comDetect.toFind = 'Arduino'
# test_object.comDetect.toFind
# test_object.comDetect.detectPort()
#
# test_object.writtingBuffer = '2766\n'
# test_object.comLayer.writeFromBuffer()
# time.sleep(int(test_object.readWriteTimeOut))
# test_object.comLayer.readToBuffer()
# test_object.readingBuffer
#
# test_object.writtingBuffer = '3039\n'
# test_object.comLayer.writeFromBuffer()
# time.sleep(int(test_object.readWriteTimeOut))
# test_object.comLayer.readToBuffer()
# test_object.readingBuffer
#
# test_object.writtingBuffer = '2730\n'
# test_object.comLayer.writeFromBuffer()
# time.sleep(int(test_object.readWriteTimeOut))
#
# for i in range(4):
#     test_object.comLayer.readToBuffer()
#
# test_object.readingBuffer
# test_object.writtingBuffer



