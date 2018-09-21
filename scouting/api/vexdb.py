import requests
from flask import g
from scouting.models.team import Team


def get_vexdb():
    if "vexdb" not in g:
        g.vexdb = VexDb()
    return g.vexdb


class VexDb:
    def __init__(self):
        self.api_url = "https://api.vexdb.io/v1"

    def get_team_by_id(self, team_name):
        """Gets team information from the VexDB API (/get_teams)."""
        resp = requests.get("%s/get_teams?team=%s" % (self.api_url, team_name))
        return Team(**resp.json())
