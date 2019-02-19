
import time
import serial


ser = serial.Serial("COM12", 9600)
ser.isOpen()

print('Enter your commands below.\r\nInsert "exit" to leave the application.')

inp=1
while 1 :
    # get keyboard input
    inp = input(">> ")
        # Python 3 users
        # input = input(">> ")
    if inp == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
        inp = 5
        k = str.encode(str(inp))

        #k = str.encode(inp)
        ser.write(k)
        ser.write(b'1')

        print(k)
        i = 0

        while True:
            response = ser.read()
            if response == b'9':
                print(response)
                i = 1
            if (i == 1):
                break

