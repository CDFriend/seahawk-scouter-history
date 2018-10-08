from flask import g

from scouting.api.firebase import get_firestore
from scouting.models.scouting_match import ScoutingMatch
from scouting.models.transaction import ScoutingTransaction


class Db:
    def __init__(self):
        self._firebase = get_firestore()

    def get_scouted_teams(self):
        """Get the team IDs of all teams we've scouted."""
        docs = self._firebase.collection("teams").get()
        return [doc.id for doc in docs]

    def get_events_for_team(self, team_id):
        """Get the SKUs of all events a team attended (or was scouted at)."""
        docs = self._firebase.collection("teams").where("team_id", "==", team_id)
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

    def commit_transaction(self, trans: ScoutingTransaction):
        for match in trans.matches:
            self._firebase.collection("matches_scouting").add(match.to_dict())


def get_db():
    if 'db' not in g:
        g.db = Db()
    return g.db
