import time
import serial

arduinoSerialPortBuffer = []
arduinoBeginCmd = b'2766\r\n'
arduinoEndCmd   = b'3039\r\n'
arduinoTelemetryCmd = b'2730\r\n' ##HEX:AAA


##Init
arduinoSerialPort = serial.Serial('COM3', 115200)

for i in range(50):
    arduinoSerialPort.write(arduinoBeginCmd)
    time.sleep(1)
    arduinoSerialPort.write(arduinoTelemetryCmd)
    time.sleep(1)
    arduinoSerialPort.write(arduinoEndCmd )
    time.sleep(1)
arduinoSerialPort.close()