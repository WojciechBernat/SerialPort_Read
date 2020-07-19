import serial.tools.list_ports


def pickOutSerialPort(deviceName, logFlag = 0):
    #Begin
    portInfo = findArduino(deviceName, logFlag)

    if portInfo != -1:
        if logFlag:
            print(portInfo)
            print(portInfo[0])
        return portInfo[0]
    else:
        return -1
    #End

def findArduino(deviceName , logFlag = 1):
    # Begin
    if logFlag:
        try:
            portList = [list(p) for p in list(serial.tools.list_ports.comports())]  ##Find serial port in use
            portList = list(portList)  ##converet to list - each item is list of single serial port

            arduinoPort = findArduinoPort(deviceName,portList) #############3

            if arduinoPort == -1:
                raise ValueError("Returned incorrect value.")
        except ValueError:
            print("ValueError: no sought serial port detected.")
        finally:
            print("Found port:", arduinoPort)  # print log
            return arduinoPort
    else:
        try:
            portList = [list(p) for p in list(serial.tools.list_ports.comports())]  ##Find serial port in use
            portList = list(portList)  ##converet to list - each item is list of single serial port

            arduinoPort = findArduinoPort(deviceName,portList) #############

            if arduinoPort == -1:
                raise ValueError("Returned incorrect value.")
        except ValueError:
            print("ValueError: no serial port detected.")
        finally:
            return arduinoPort
    # End

def findArduinoPort(deviceName, argList):
    # Begin
    for i in argList:

        for j in i:
            if (j.find(deviceName) != -1):
                return i

    return -1
    # end

print(findArduino("ASFA", 0))

print(pickOutSerialPort("Arduino Uno", 0))

unoPort = pickOutSerialPort("Arduino Uno", 0)
arduinoSerialPort = serial.Serial(unoPort, 115200, timeout=0.2, write_timeout=0.2)