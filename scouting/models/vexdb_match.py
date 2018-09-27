class VexdbMatch:
    def __init__(self, **kwargs):
        self.event_sku = str(kwargs["sku"])
        self.matchnum = int(kwargs["matchnum"])

        self.red1 = str(kwargs["red1"])
        self.red2 = str(kwargs["red2"])
        self.red3 = str(kwargs["red3"])
        self.redsit = str(kwargs["redsit"])

        self.blue1 = str(kwargs["blue1"])
        self.blue2 = str(kwargs["blue2"])
        self.blue3 = str(kwargs["blue3"])
        self.bluesit = str(kwargs["bluesit"])

        self.red_score = int(kwargs["redscore"])
        self.blue_score = int(kwargs["bluescore"])

    def get_red_teams(self):
        if self.red3:
            teams = [self.red1, self.red2, self.red3]
            teams.remove(self.redsit)
            return teams
        else:
            return [self.red1, self.red2]

    def get_blue_teams(self):
        if self.blue3:
            teams = [self.blue1, self.blue2, self.blue3]
            teams.remove(self.bluesit)
            return teams
        else:
            return [self.blue1, self.blue2]
