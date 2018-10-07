from datetime import date
from scouting.models.scouting_match import ScoutingMatch


class ScoutingTransaction:
    def __init__(self, submitdate=date.today()):
        self.matches = []
        self.submit_date = submitdate

    def add_match(self, match: ScoutingMatch):
        self.matches.append(match)
