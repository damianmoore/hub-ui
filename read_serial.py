from time import sleep

import serial


def main():
    ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=0)

    while True:
        data = ser.read(255).strip()
        if data:
            print(data)
        sleep(0.1)


if __name__ == '__main__':
    main()
