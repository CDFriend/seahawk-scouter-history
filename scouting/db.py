from flask import g

# TODO: get actual firebase impl going
from scouting.api.mock.firebase import Client
from scouting.models.scouting_match import ScoutingMatch


class Db:
    def __init__(self):
        self._firebase = Client()

    def get_all_matches(self):
        docs = self._firebase.collection("matches_scouting").get()
        return [ScoutingMatch(**doc.to_dict()) for doc in docs]


def get_db():
    if 'db' not in g:
        g.db = Db()
    return g.db
