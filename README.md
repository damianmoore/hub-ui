# Hub-UI

This project is about creating a physical electronic user interface. It consists
of a charater-based LCD screen based on the
[HD44780](https://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller)
interface and a [rotary
encoder](https://en.wikipedia.org/wiki/Rotary_encoder#Incremental_rotary_encoder)
dial which can register clockwise, anti-clockwise and push button motion.

The interface is designed for controlling a small home entertainment hub -
selecting radio stations, setting alarms, showing notifications etc.

An Arduino Nano reads changes of rotary encoder, which then transmits these
events over a Serial-USB connection. A Raspberry Pi is connected to the Arduino
over USB and to the LCD display using the GPIO pins.

## Menus

A large part of the project is the menu navigation. The menu structure is
defined in `settings.py` with a nested list/dict. Methods to be called on
selection of a menu item are stored in the `Controller` class. Names of the menu
items can also be a method name which make them dynamically generated on draw.

When trialling your own menu structure you can use the `simulator.py` script by
using Up/Down arrow and Enter keys.

## Other Screens

You may want to create other screens that don't follow the basic nested menu
structure. You can inherit from the `Screen` class as `Menu` does. There are no
examples of this yet. This will probably be attempted soon with a volume slider.

## Production

The `service.py` script is what gets run in production. It takes input from the
Arduino serial device and will soon output to the LCD.

## Other scripts

`read_serial.py` is utility to help get serial communication working. It will
print characters that get sent from the rotary encoder/Arduino.
