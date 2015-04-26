class Screen(object):
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.clear()

    def clear(self):
        self.buffer = [' '*self.columns for i in range(self.rows)]

    def show(self):
        for row in self.buffer:
            print(row)
