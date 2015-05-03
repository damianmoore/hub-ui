class Screen(object):
    def __init__(self, columns, rows, output='terminal'):
        self.columns = columns
        self.rows = rows
        self.output = output
        self.clear()

        if output == 'lcd':
            from lcd import lcd_init, lcd_string, lcd_byte_line, LCD_CMD
            lcd_init()

    def clear(self):
        self.buffer = [' '*self.columns for i in range(self.rows)]

    def show(self):
        if self.output == 'lcd':
            for i, row in enumerate(self.buffer):
                lcd_byte_line(i, LCD_CMD)
                lcd_string(row, 1)
        elif self.output == 'terminal':
            print('+{}+'.format('-'*self.columns))
            for row in self.buffer:
                print('|{}{}|'.format(row[:self.columns], ' '*(self.columns-len(row))))
            print('+{}+'.format('-'*self.columns))
