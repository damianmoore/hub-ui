from time import sleep

import serial

from settings import MENU_STRUCTURE
from menu import Menu
from screen import Screen


def main():
    ser = serial.Serial('/dev/ttyAMA0', 7600, timeout=0)

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


def cleanup():
    Screen(20, 4, output='lcd').clear()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
