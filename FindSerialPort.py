import serial.tools.list_ports


def findArduino(logFlag=1):
    # Begin
    if logFlag:
        try:
            portList = [list(p) for p in list(serial.tools.list_ports.comports())]  ##Find serial port in use
            portList = list(portList)  ##converet to list - each item is list of single serial port

            arduinoPort = findArduinoPort(portList)

            if arduinoPort == -1:
                raise ValueError("Returned incorrect value.")
        except ValueError:
            print("ValueError: no Arduino serial port detected.")
        finally:
            print("Found Arduino port:", arduinoPort)  # print log
            return arduinoPort
    else:
        try:
            portList = [list(p) for p in list(serial.tools.list_ports.comports())]  ##Find serial port in use
            portList = list(portList)  ##converet to list - each item is list of single serial port

            arduinoPort = findArduinoPort(portList)

            if arduinoPort == -1:
                raise ValueError("Returned incorrect value.")
        except ValueError:
            print("ValueError: no Arduino serial port detected.")
        finally:
            return arduinoPort
    # End


def findArduinoPort(argList):
    # Begin
    for i in argList:

        for j in i:
            if (j.find("Arduino Uno") != -1):
                return i

    return -1
    # end


findArduino()
