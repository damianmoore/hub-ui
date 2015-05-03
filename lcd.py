# HD44780 20x4 LCD Display
#
# Based on code by Matt Hawkins from this tutorial:
# http://www.raspberrypi-spy.co.uk/2012/08/20x4-lcd-module-control-using-python/


import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
LED_ON = 4

# Define some device constants
LCD_WIDTH = 20  # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

# Timing constants
E_PULSE = 0.000001
E_DELAY = 0.000001


def lcd_init():
    GPIO.setmode(GPIO.BCM)        # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)   # E
    GPIO.setup(LCD_RS, GPIO.OUT)  # RS
    GPIO.setup(LCD_D4, GPIO.OUT)  # DB4
    GPIO.setup(LCD_D5, GPIO.OUT)  # DB5
    GPIO.setup(LCD_D6, GPIO.OUT)  # DB6
    GPIO.setup(LCD_D7, GPIO.OUT)  # DB7
    GPIO.setup(LED_ON, GPIO.OUT)  # Backlight enable

    # Initialise display
    lcd_byte(0x33, LCD_CMD)
    lcd_byte(0x32, LCD_CMD)
    lcd_byte(0x28, LCD_CMD)
    lcd_byte(0x0C, LCD_CMD)
    lcd_byte(0x06, LCD_CMD)
    lcd_byte(0x01, LCD_CMD)

    GPIO.output(LED_ON, True)


def lcd_string(message, style):
    # Send string to display
    # style=1 Left justified
    # style=2 Centred
    # style=3 Right justified

    if style==1:
        message = message.ljust(LCD_WIDTH, ' ')
    elif style==2:
        message = message.center(LCD_WIDTH, ' ')
    elif style==3:
        message = message.rjust(LCD_WIDTH, ' ')

    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)


def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True    for character
    #                False for command

    GPIO.output(LCD_RS, mode) # RS

    # High bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x10==0x10:
        GPIO.output(LCD_D4, True)
    if bits&0x20==0x20:
        GPIO.output(LCD_D5, True)
    if bits&0x40==0x40:
        GPIO.output(LCD_D6, True)
    if bits&0x80==0x80:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)

    # Low bits
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits&0x01==0x01:
        GPIO.output(LCD_D4, True)
    if bits&0x02==0x02:
        GPIO.output(LCD_D5, True)
    if bits&0x04==0x04:
        GPIO.output(LCD_D6, True)
    if bits&0x08==0x08:
        GPIO.output(LCD_D7, True)

    # Toggle 'Enable' pin
    time.sleep(E_DELAY)
    GPIO.output(LCD_E, True)
    time.sleep(E_PULSE)
    GPIO.output(LCD_E, False)
    time.sleep(E_DELAY)


def lcd_byte_line(line, mode):
    bit_map = [
        0x80, # LCD RAM address for the 1st line
        0xC0, # LCD RAM address for the 2nd line
        0x94, # LCD RAM address for the 3rd line
        0xD4, # LCD RAM address for the 4th line
    ]
    bits = bit_map[line]
    lcd_byte(bits, mode)
