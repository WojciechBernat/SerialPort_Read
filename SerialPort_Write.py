import time

import serial

arduinoSerialReadingBuffer = []
arduinoBeginCmd = '2766\n'
arduinoEndCmd = '3039\n'
arduinoTelemetryCmd = '2730\n'  ##HEX:AAA

byteToRead = 0
readWriteTimeOut = 0.1
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
    time.sleep(readWriteTimeOut)  # Dead time between write command and read slave's response
    # read response
    # if (cmd == arduinoTelemetryCmd):
    #     for i in range(4):
    #         readToBuffer(readBuffer, serialPortInstance)
    # else:
    #     readToBuffer(readBuffer, serialPortInstance)
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
arduinoSerialPort = serial.Serial('COM3', 115200, timeout=1.49, write_timeout=0.1)

arduinoSerialPort.write(bytearray(arduinoTelemetryCmd, 'utf-8'))  ##Send command to slave
time.sleep(readWriteTimeOut)  # Dead time between write command and read slave's response
arduinoSerialReadingBuffer.append(arduinoSerialPort.read())

executeCommand(arduinoSerialPort, arduinoTelemetryCmd, arduinoSerialReadingBuffer, readWriteTimeOut)

# for i in range(50):
#     print("First command:", arduinoBeginCmd)
#     arduinoSerialPort.write(bytearray(arduinoBeginCmd, 'utf-8'))
#     time.sleep(wrTimeOut)
#     byteToRead = arduinoSerialPort.inWaiting()
#     arduinoSerialReadingBuffer[:]
#     arduinoSerialReadingBuffer = arduinoSerialPort.read(byteToRead)
#     arduinoSerialReadingBuffer = arduinoSerialPort.readline()
#     if arduinoSerialReadingBuffer:
#         print("read:", arduinoSerialReadingBuffer)
#
#     arduinoSerialReadingBuffer[:]
#     time.sleep(deadTimeOut)
#
#     print("Second command: ", arduinoTelemetryCmd)
#     arduinoSerialPort.write(bytearray(arduinoTelemetryCmd, 'utf-8'))
#     # time.sleep(0.1)
#     time.sleep(wrTimeOut)
#     arduinoSerialReadingBuffer[:]
#     arduinoSerialReadingBuffer = arduinoSerialPort.readline()
#
#     if arduinoSerialReadingBuffer:
#         print("read:", arduinoSerialReadingBuffer)
#
#     arduinoSerialReadingBuffer[:]
#     time.sleep(deadTimeOut)
#
#     print("Third command: ", arduinoEndCmd)
#     arduinoSerialPort.write(bytearray(arduinoEndCmd, 'utf-8'))
#     time.sleep(wrTimeOut)
#     arduinoSerialReadingBuffer = arduinoSerialPort.readline()
#
#     if arduinoSerialReadingBuffer:
#         print("read:", arduinoSerialReadingBuffer)
#
#     time.sleep(deadTimeOut)

arduinoSerialPort.close()
