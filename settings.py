RADIO_STATIONS = [
    ('Secret Agent', 'sa.pls'),
    ('Dubstep Beyond', 'db.pls'),
]


class Controller(object):
    radio_on = False
    radio_station = 0

    def radio_state(self):
        state = self.radio_on and 'ON' or 'OFF'
        return 'State: {}'.format(state)

    def radio_toggle(self):
        self.radio_on = not self.radio_on

    def radio_selected(self):
        return 'Station: {}'.format(RADIO_STATIONS[self.radio_station][0])

    def radio_select(self, index):
        self.radio_station = index

    def radio_stations(self):
        stations = []
        for i, station in enumerate(RADIO_STATIONS):
            stations.append(
                {'name': station[0], 'on_select': 'radio_select,back', 'on_select_params': {'index': i}}
            )
        return stations


structure = {
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
    ],
}
