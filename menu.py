from settings import Controller
from screen import Screen


class Menu(Screen):
    selected = [0,]
    scroll_offset = 0

    def __init__(self, structure, *args, **kwargs):
        self.structure = structure
        self.controller = Controller()
        super(Menu, self).__init__(*args, **kwargs)
        self.draw()

    def get_current_menu(self):
        menu = self.structure

        for i in self.selected[:-1]:
            menu = menu['items'][i]

        # Menu list could be a method name so try calling it.
        if isinstance(menu['items'], str):
            try:
                menu['items'] = getattr(self.controller, menu['items'])()
            except AttributeError:
                pass

        if len(self.selected) > 1 and menu['items'][-1]['name'] != '< Back':
            menu['items'].append({'name': '< Back', 'on_select': 'back'})
        return menu

    def draw(self):
        self.clear()
        menu = self.get_current_menu()

        # Control the scroll up and down based on the cursor position
        if self.selected[-1] > self.scroll_offset + (len(self.buffer) - 1):
            self.scroll_offset = self.selected[-1] - (len(self.buffer) - 1)
        elif self.selected[-1] < self.scroll_offset:
            self.scroll_offset = self.selected[-1]

        # Draw the visible items to the buffer along with cursor
        for i, row in enumerate(self.buffer):
            try:
                if i + self.scroll_offset == self.selected[-1]:
                    line = '> '
                else:
                    line = '  '

                item = menu['items'][i + self.scroll_offset]['name']
                try:
                    line += getattr(self.controller, item)()
                except AttributeError:
                    line += item
                self.buffer[i] = line
            except IndexError:
                pass

    def select(self):
        menu = self.get_current_menu()
        item = menu['items'][self.selected[-1]]
        going_back = False
        self.scroll_offset = 0

        if 'on_select' in item:
            kwargs = item.get('on_select_params', {})
            for method in item['on_select'].split(','):
                if method == 'back':
                    going_back = True
                else:
                    getattr(self.controller, method)(**kwargs)

        if going_back:
            self.selected.pop()
        elif 'items' in item:
            self.selected.append(0)
        self.draw()

    def down(self):
        if self.selected[-1] < len(self.get_current_menu()['items']) - 1:
            self.selected[-1] += 1
        else:
            self.selected[-1] = 0
        self.draw()

    def up(self):
        if self.selected[-1] > 0:
            self.selected[-1] -= 1
        else:
            self.selected[-1] = len(self.get_current_menu()['items']) - 1
        self.draw()
