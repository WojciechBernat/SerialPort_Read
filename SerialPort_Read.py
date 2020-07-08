#Program which reads data from serial prot.
#Also my first program in python. Wow! Awsome!

import serial
import time


def calcAverageTemp(mylist):
    sumList = sum(mylist)
    avgTemp = sumList/ (len(mylist))
    return avgTemp;

arduinoSerialPort = serial.Serial('COM3', 115200)
arduinoInternalTemp = []

for i in range(32):
    readVal = arduinoSerialPort.readline()        ##read value

    tmpStr = readVal.decode()            # decode byte string into Unicode
    tmpStr = tmpStr.rstrip()             # remove \n and \r
    internalTemperature = float(tmpStr)  # convert string to float
    print("internal temp:", internalTemperature)

    arduinoInternalTemp.append(internalTemperature)     ##add new measurement to list
    time.sleep(0.1)

arduinoSerialPort.close()

print ("Calc average temperature")

print ("AvgTemp:", calcAverageTemp(arduinoInternalTemp))



