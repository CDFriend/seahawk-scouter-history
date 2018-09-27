from flask import g

# TODO: get actual firebase impl going
from scouting.api.mock.firebase import Client
from scouting.models.scouting_match import ScoutingMatch


class Db:
    def __init__(self):
        self._firebase = Client()

    def get_scouted_teams(self):
        """Get the team IDs of all teams we've scouted."""
        docs = self._firebase.collection("teams").get()
        return [doc.id for doc in docs]

    def get_all_events(self):
        """Get the SKUs of all events we've scouted."""
        docs = self._firebase.collection("events").get()
        return [doc.id for doc in docs]

    def get_all_matches(self):
        """Get data from ALL scouted matches."""
        docs = self._firebase.collection("matches_scouting").get()
        return [ScoutingMatch(**doc.to_dict()) for doc in docs]

    def get_matches_for_event_id(self, id):
        """Get match data for a given tournament ID."""
        docs = self._firebase.collection("matches_scouting")\
                .where("tournament_sku", "==", id)
        return [ScoutingMatch(**doc.to_dict()) for doc in docs]


def get_db():
    if 'db' not in g:
        g.db = Db()
    return g.db
