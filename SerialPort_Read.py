# Program which reads data from serial prot.
# Also my first program in python. Wow! Awsome!

import time
import serial

def calcAverageTemp(mylist):
    length = len(mylist)
    if(length <= 0):
        return -1
    else :
        sumList = sum(mylist)
        avgTemp = sumList / (length)
        return avgTemp;

startWord = "Start"
frameCounter = 0

internalTemperature = []
voltage1 = []
voltage2 = []
batteryVoltage = []

arduinoSerialPort = serial.Serial('COM3', 115200)

for i in range(100):
    readVal = arduinoSerialPort.readline()  ##read value
    print("Reading value:", readVal)
    tmpStr = readVal.decode()  # decode byte string into Unicode
#   print("TmpString: ", tmpStr)
    tmpStr = tmpStr.rstrip()  # remove \n and \r
#   print("TmpString: ", tmpStr)

    if (tmpStr == startWord):  # detect start word
        frameCounter = 1
        print("Detected start word!")
    else:
        data = float(tmpStr)  # convert string to float
        if (frameCounter == 1):
            internalTemperature.append(data)
#            print("internal temp:", internalTemperature)
            frameCounter += 1
        elif (frameCounter == 2):
            voltage1.append(data)
#            print("1st motor's voltage:", voltage1)
            frameCounter += 1
        elif (frameCounter == 3):
            voltage2.append(data)
#            print("2nd motor's voltage:", voltage2)
            frameCounter += 1
        elif (frameCounter == 4):
            batteryVoltage.append(data)
#            print("Battery voltage:", batteryVoltage)
            frameCounter = 0
        else:
            frameCounter = 0
    time.sleep(0.1)

arduinoSerialPort.close()

print("Average temperature:", calcAverageTemp(internalTemperature))
print("Average 1st motor voltage:", calcAverageTemp(voltage1))
print("Average 2nd motor voltage:", calcAverageTemp(voltage2))
print("Average main battery voltage:", calcAverageTemp(batteryVoltage))

print("Length temperature:", len(internalTemperature))
print("Length 1st voltage:", len(voltage1))
print("Length 2nd voltge:", len(voltage2))
print("Length battery:", len(batteryVoltage))
