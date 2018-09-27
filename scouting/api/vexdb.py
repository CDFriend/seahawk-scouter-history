import requests
from flask import g

from scouting.models.team import Team
from scouting.models.event import Event
from scouting.models.vexdb_match import VexdbMatch


def get_vexdb():
    if "vexdb" not in g:
        g.vexdb = VexDb()
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

    def get_event_by_sku(self, sku):
        resp = requests.get("%s/get_events?sku=%s" % (self.api_url, sku)).json()
        if resp["size"] <= 0:
            raise CouldNotFindError()
        result = resp["result"][0]
        return Event(**result)

    def get_matches_for_event(self, sku):
        resp = requests.get("%s/get_matches?sku=%s" % (self.api_url, sku)).json()
        if resp["size"] <= 0:
            return []
        return [VexdbMatch(**match_info) for match_info in resp["result"] if match_info["scored"]]
