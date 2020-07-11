import time
import serial

##List, variables, const
arduinoSerialPortBuffer = []
arduinoBeginCmd = b'2766\r\n'

temperatureBuffer = []
voltageBuffer_1 = []
voltageBuffer_2 = []
batteryBuffer = []

##Init objects
arduinoSerialPort = serial.Serial('COM3', 115200)

##Functions
def detectBeginTransmission(List, startCommand):
    if ((List[0]) == startCommand):
        print("Detected transmission's command.")
        return 1;
    else:
        return -1;


def decodeStringToFloat(sourceList):
    destinyList = [float(i) for i in sourceList]
    print("Destiny list: ", destinyList)
    return destinyList;

def decodeFrame(sourceList, tempList, voltList_1,voltList_2, batteryList):
    floatList = decodeStringToFloat(sourceList)
    print("float list:", floatList)
    tempList.append(floatList[1])
    voltList_1.append(floatList[2])
    voltList_2.append(floatList[3])
    batteryList.append(floatList[4])

    print("Temp buffer:", tempList)
    print("1st voltage: ", voltList_1)
    print("2nd voltage: ", voltList_2)
    print("Battery voltage: ", batteryList)


##Code
if (arduinoSerialPort.isOpen() == False):
    arduinoSerialPort.open()

for i in range(6):
    # start reading to buffer
    arduinoSerialPortBuffer.append(arduinoSerialPort.read_until('\n', 6))  # read and append to buffer


arduinoSerialPort.close()

detectBeginTransmission(arduinoSerialPortBuffer, arduinoBeginCmd)
print("Buffer: ", arduinoSerialPortBuffer)
print("Buffer's length: ", len(arduinoSerialPortBuffer))

decodeFrame(arduinoSerialPortBuffer, temperatureBuffer, voltageBuffer_1,voltageBuffer_2, batteryBuffer)
#decodeStringToFloat( arduinoSerialPortBuffer)







