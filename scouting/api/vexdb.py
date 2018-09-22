import requests
from flask import g
from scouting.models.team import Team


def get_vexdb():
    if "vexdb" not in g:
        g.vexdb = VexDbDummy()
    return g.vexdb


class CouldNotFindError(BaseException):
    pass


class VexDb:
    def __init__(self):
        self.api_url = "https://api.vexdb.io/v1"

    def get_team_by_id(self, team_num):
        """Gets team information from the VexDB API (/get_teams)."""
        resp = requests.get("%s/get_teams?team=%s" % (self.api_url, team_num)).json()
        if resp["size"] <= 0:
            raise CouldNotFindError()
        result = resp["result"][0]
        return Team(**result)


class VexDbDummy:
    """Mock VexDb interface for testing."""
    def get_team_by_id(self, team_num):
        if team_num not in self.team_data:
            raise CouldNotFindError()
        return Team(**self.team_data[team_num])

    team_data = {
        "9181A": {
            "number": "9181A",
            "program": "VEX Robotics Competition",
            "team_name": "Rainbow Fabricators",
            "robot_name": "Bill",
            "organisation": "Seaquam Secondary",
            "city": "Delta",
            "region": "British Columbia",
            "country": "Canada",
            "grade": "Middle/High School",
            "is_registered": True
        }
    }
