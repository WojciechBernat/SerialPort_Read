import time

import serial

arduinoSerialReadingBuffer = []
arduinoBeginCmd = '2766\n'
arduinoEndCmd = '3039\n'
arduinoTelemetryCmd = '2730\n'  ##HEX:AAA

byteToRead = 0
readWriteTimeOut = 1.5
deadTimeOut = 1


def executeCommand(serialPortInstance, cmd, readBuffer, readWriteTimeOut):
    # validate arguments
    if (readWriteTimeOut < 0):
        readWriteTimeOut = 0

    # Begin
    print("Execute command:", cmd)

    serialPortInstance.reset_output_buffer()
    serialPortInstance.reset_input_buffer()
    clearBuffer(readBuffer)  # preclear buffer

    serialPortInstance.write(bytearray(cmd, 'utf-8'))  ##Send command to slave
    serialPortInstance.flush()
    time.sleep(readWriteTimeOut)  # Dead time between write command and read slave's response

    readBuffer.append(serialPortInstance.read_until('\n', 150))
    if readBuffer:
        print("Read buffer: ", readBuffer)

    serialPortInstance.reset_output_buffer()
    serialPortInstance.reset_input_buffer()
    # End


def readToBuffer(buffer, serialPortInstance):
    # Begin
    if isinstance(buffer, list):
        buffer.append(serialPortInstance.read_until('\n', 150))
    else:
        buffer = serialPortInstance.readline()
    # End


def clearBuffer(buffer):
    # Begin
    if isinstance(buffer, list):
        buffer.clear()
    elif isinstance(buffer, str):
        buffer = '0'
    elif isinstance(buffer, int):
        buffer = 0
    else:
        print("Unsupported type. Cannot clean buffer.")
    # End


##Init
arduinoSerialPort = serial.Serial('COM3', 115200, timeout=0.2, write_timeout=0.2)


executeCommand(arduinoSerialPort, arduinoBeginCmd, arduinoSerialReadingBuffer, readWriteTimeOut)
executeCommand(arduinoSerialPort, arduinoEndCmd, arduinoSerialReadingBuffer, readWriteTimeOut)
executeCommand(arduinoSerialPort, arduinoTelemetryCmd, arduinoSerialReadingBuffer, readWriteTimeOut)
executeCommand(arduinoSerialPort, arduinoBeginCmd, arduinoSerialReadingBuffer, readWriteTimeOut)
executeCommand(arduinoSerialPort, arduinoEndCmd, arduinoSerialReadingBuffer, readWriteTimeOut)
executeCommand(arduinoSerialPort, arduinoTelemetryCmd, arduinoSerialReadingBuffer, readWriteTimeOut)


arduinoSerialPort.close()
