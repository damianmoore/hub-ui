from time import sleep

import serial

from settings import structure
from menu import Menu


def main():
    ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=0)

    menu = Menu(structure, 20, 4)

    def show():
        for i in range(20):
            print('')
        menu.show()

    show()

    while True:
        data = ser.read(255).strip()
        if data:
            if data == 'c':     # clockwise
                menu.down()
            elif data == 'a':   # anti-clockwise
                menu.up()
            elif data == 'p':   # press
                menu.select()
            show()
        sleep(0.01)


if __name__ == '__main__':
    main()
