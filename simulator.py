#!/usr/bin/env python

from settings import MENU_STRUCTURE
from menu import Menu
from utils import getch


def main():
    menu = Menu(MENU_STRUCTURE, 20, 4, output='terminal')

    def show():
        for i in range(20):
            print('')
        menu.show()

    show()
    kgen = getch(0.1)

    while True:
        key = kgen.next()

        if key:
            if key == 'B':
                menu.down()
            elif key == 'A':
                menu.up()
            elif key in [' ', '\n']:
                menu.select()
            show()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
