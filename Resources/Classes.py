from datetime import datetime as dt

class TimeContainer():
    def setera(self):
        currTime = int(self.time.strftime('%H'))
        if currTime < 12:
            self.era = "Morning"
        elif currTime >= 12 and currTime < 18:
            self.era = "Afternoon"
        else:
            self.era = "Evening"
    def __init__(self):
        self.time = dt.now()
        self.day = self.time.strftime('%A')
        self.setera()

class Phrase(TimeContainer):
    def __init__(self, opener, adj, food, connector):
        super().__init__()
        self.opener = opener
        self.adj = adj
        self.food = food
        self.connector = connector