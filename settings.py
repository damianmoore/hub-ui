import math
import re

from utils import run_cmd


RADIO_STATIONS = [
    ('Secret Agent', 'http://somafm.com/startstream=secretagent.pls'),
    ('Dubstep Beyond', 'http://somafm.com/startstream=dubstep.pls'),
    ('Suburbs of Goa', 'http://somafm.com/startstream=suburbsofgoa.pls'),
    ('Groove Salad', 'http://somafm.com/startstream=groovesalad.pls'),
]

VOLUME_VALUES = [i*10 for i in range(11)]
VOLUME_ITEMS = []
for i in VOLUME_VALUES:
    VOLUME_ITEMS.append({'name': '{}%'.format(i), 'on_select': 'volume_set,back', 'on_select_params': {'value': i}},)


class Controller(object):
    radio_on = False
    radio_station = 0
    volume = 0

    def __init__(self, *args, **kwargs):
        self.volume = self.volume_from_mixer()

    def radio_state(self):
        state = self.radio_on and 'ON' or 'OFF'
        return 'State: {}'.format(state)

    def radio_toggle(self):
        self.radio_on = not self.radio_on
        if self.radio_on:
            run_cmd('mpc stop')
            self.radio_select(self.radio_station)
            run_cmd('mpc play')
        else:
            run_cmd('mpc stop')

    def radio_selected(self):
        return 'Station: {}'.format(RADIO_STATIONS[self.radio_station][0])

    def radio_select(self, index):
        self.radio_station = index
        run_cmd('mpc clear')
        run_cmd('mpc load {}'.format(RADIO_STATIONS[self.radio_station][1]))
        run_cmd('mpc play')

    def radio_stations(self):
        stations = []
        for i, station in enumerate(RADIO_STATIONS):
            stations.append(
                {'name': station[0], 'on_select': 'radio_select,back', 'on_select_params': {'index': i}}
            )
        return stations

    def volume_state(self):
        return 'Volume: {}%'.format(self.volume)

    def volume_set(self, value):
        self.volume = value
        self.volume_to_mixer(value)

    def volume_to_mixer(self, value):
        value = round(math.sqrt(value)*10)
        run_cmd('amixer sset \'PCM\' {}%'.format(value))

    def volume_from_mixer(self):
        response = run_cmd('amixer sget \'PCM\'')
        matches = re.findall('[0-9]*%', response)
        if matches:
            percent = int(matches[0].rstrip('%'))
            percent = round((percent/10.0)**2)
            nearest = 0
            distance = 100
            for i in VOLUME_VALUES:
                if abs(percent - i) < distance:
                    nearest = i
                    distance = abs(percent - i)
            print nearest
            return nearest
        return 0


MENU_STRUCTURE = {
    'items': [
        {
            'name': 'Radio',
            'items': [
                {'name': 'radio_state', 'on_select': 'radio_toggle'},
                {'name': 'radio_selected', 'items': 'radio_stations'},
            ],
        },
        {
            'name': 'Alarm',
            'items': [
                {'name': 'New alarm'},
                {'name': 'Change alarm 1'},
            ],
        },
        {
            'name': 'volume_state',
            'items': VOLUME_ITEMS
        },
    ],
}
