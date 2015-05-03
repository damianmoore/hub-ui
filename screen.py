class Screen(object):
    def __init__(self, columns, rows, output='terminal'):
        self.columns = columns
        self.rows = rows
        self.output = output
        self.clear()

        if output == 'lcd':
            import lcd
            self.lcd = lcd
            self.lcd.lcd_init()

    def clear(self):
        self.buffer = [' '*self.columns for i in range(self.rows)]

    def show(self):
        if self.output == 'lcd':
            for i, row in enumerate(self.buffer):
                self.lcd.lcd_byte_line(i, self.lcd.LCD_CMD)
                self.lcd.lcd_string(row, 1)
        elif self.output == 'terminal':
            print('+{}+'.format('-'*self.columns))
            for row in self.buffer:
                print('|{}{}|'.format(row[:self.columns], ' '*(self.columns-len(row))))
            print('+{}+'.format('-'*self.columns))
