from settings import structure
from menu import Menu
from utils import getch


def main():
    menu = Menu(structure, 20, 4)

    def show():
        for i in range(20):
            print('')
        menu.show()

    show()
    kgen = getch(0.1)

    while True:
        key = kgen.next()

        if key == 'B':
            menu.down()
            show()
        elif key == 'A':
            menu.up()
            show()
        elif key in [' ', '\n']:
            menu.select()
            show()


if __name__ == '__main__':
    main()
