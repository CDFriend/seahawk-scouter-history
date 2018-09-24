import re
from scouting.utils import get_location_str


def validate_team_id(team_id):
    """Checks whether or not a team ID string is valid."""
    return re.match("^\d+[A-Za-z]+$", team_id) is not None


class Team:
    def __init__(self, **kwargs):
        self.id            = str(kwargs["number"])
        self.program       = str(kwargs["program"])
        self.team_name     = str(kwargs["team_name"])
        self.robot_name    = str(kwargs["robot_name"])
        self.organization  = str(kwargs["organisation"])
        self.city          = str(kwargs["city"])
        self.region        = str(kwargs["region"])
        self.country       = str(kwargs["country"])
        self.grade         = str(kwargs["grade"])
        self.is_registered = bool(kwargs["is_registered"])

    def get_location_str(self):
        return get_location_str(self.city, self.region, self.country)
