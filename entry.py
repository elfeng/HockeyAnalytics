class Entry:
    entrycount = 0;

    def __init__(self):
        self.count = entrycount
        entrycount += 1
        self.initiating_player = ""
        self.coords = []
        self.time_in_zone = 0
        self.style = ""
        self.success = False

    def initiate_player(self, name):
        self.initiating_player = player

    def add_coords(self, coordinates):
        self.coords = coordinates

    def add_time(self, time):
        self.time_in_zone = time

    def add_style(self, style_string):
        self.style = style

    def set_success(self):
        self.success = True

    def dump(self):
        return {"Entry %d" % self.count: {'style': self.style,
                               'success': self.success,
                               'initiating_player': self.initiating_player,
                               'coords': self.coords
                               'time_in_zone': self.time_in_zone}}
