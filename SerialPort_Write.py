import time
import serial

arduinoSerialPortBuffer = []
arduinoSerialReadingBuffer = []
arduinoBeginCmd = '2766\n'
arduinoEndCmd   = '3039\n'
arduinoTelemetryCmd = '2730\n' ##HEX:AAA

byteToRead = 0
wrTimeOut = 0.1
deadTimeOut = 0.5

##Init
arduinoSerialPort = serial.Serial('COM3', 115200,timeout=0.1, write_timeout=0.1)

for i in range(50):
    print("First command:", arduinoBeginCmd)
    arduinoSerialPort.write(bytearray(arduinoBeginCmd, 'utf-8'))
    # time.sleep(0.1)
    time.sleep(wrTimeOut)
    byteToRead = arduinoSerialPort.inWaiting()
    arduinoSerialReadingBuffer[:]
    arduinoSerialReadingBuffer = arduinoSerialPort.read(byteToRead)

    if arduinoSerialReadingBuffer:
        print("read:" , arduinoSerialReadingBuffer)

    arduinoSerialReadingBuffer[:]
    time.sleep(deadTimeOut)

    print("Second command: " , arduinoTelemetryCmd)
    arduinoSerialPort.write(bytearray(arduinoTelemetryCmd, 'utf-8'))
    # time.sleep(0.1)
    time.sleep(wrTimeOut)
    arduinoSerialReadingBuffer[:]
    arduinoSerialReadingBuffer = arduinoSerialPort.readline()

    if arduinoSerialReadingBuffer:
        print("read:" , arduinoSerialReadingBuffer)

    arduinoSerialReadingBuffer[:]
    time.sleep(deadTimeOut)

    print("Third command: " , arduinoEndCmd)
    arduinoSerialPort.write(bytearray(arduinoEndCmd, 'utf-8'))
    time.sleep(wrTimeOut)
    arduinoSerialReadingBuffer = arduinoSerialPort.readline()

    if arduinoSerialReadingBuffer:
        print("read:", arduinoSerialReadingBuffer)


    time.sleep(deadTimeOut)

arduinoSerialPort.close()