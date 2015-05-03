from time import sleep

import serial

from settings import MENU_STRUCTURE
from menu import Menu


def main():
    ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=0)

    menu = Menu(MENU_STRUCTURE, 20, 4, output='lcd')
    menu.show()

    while True:
        data = ser.read(8).strip()

        if data:
            if data == 'c':     # clockwise
                menu.down()
            elif data == 'a':   # anti-clockwise
                menu.up()
            elif data == 'p':   # press
                menu.select()
            menu.show()
        sleep(0.01)


if __name__ == '__main__':
    main()
