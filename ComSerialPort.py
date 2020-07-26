import serial


#Communication with serial port class
class ComSerialPort:
    errorFlag = 0
    def __init__(self,serialPortInstance, writeBuffer, readBuffer):
        try:
            if (type(serialPortInstance) != serial):
                raise TypeError
            else:
                self.__serialPortInstance = serialPortInstance
                print("Correct type of serial port instances.")
        except:
            print("Incorrect type of serial port instances.")

        try:
            if((type(writeBuffer) || type(readBuffer)) != list):
                raise TypeError
            else:
                self.__writeBuffer = writeBuffer
                self.__readBuffer = readBuffer
                print("Correct type of read/write buffers.")
        except:
            print("Incorrect type of read/write buffers. Buffers must be list.")




    def readToBuffer(self):
        self.__readBuffer.append(self.__serialPortInstance.read_until('\n', 32))

    def writeFromBuffer(self):
        self.__serialPortInstance.write