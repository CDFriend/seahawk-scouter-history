from flask import g

from scouting.api.firebase import get_firestore
from scouting.models.stats import Stats
from scouting.models.scouting_match import ScoutingMatch
from scouting.models.transaction import ScoutingTransaction


class Db:
    def __init__(self):
        self._firebase = get_firestore()

    def get_team_stats(self, team_id):
        """Get stats for a given team ID"""
        doc = self._firebase.collection("teams").document(team_id)
        return Stats(**doc.get().to_dict()["stats"])

    def get_scouted_teams(self):
        """Get the team IDs of all teams we've scouted."""
        docs = self._firebase.collection("teams").get()
        return [doc.id for doc in docs]

    def get_events_for_team(self, team_id):
        """Get the SKUs of all events a team attended (or was scouted at)."""
        team = self._firebase.collection("teams").document(team_id).get().to_dict()
        return [event_ref.id for event_ref in team["events"]]

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
        event = self._firebase.collection("events").document(id).get().to_dict()

        # Convert firebase dictionary to our format
        matches = []
        for doc_ref in event["matches"]:
            match_dict = doc_ref.get().to_dict()

            # firebase DocumentReference -> string
            match_dict["team_id"] = match_dict["team_id"].id

            matches.append(ScoutingMatch(**match_dict))

        return matches

    def commit_transaction(self, trans: ScoutingTransaction):
        for match in trans.matches:
            self._firebase.collection("matches_scouting").add(match.to_dict())


def get_db():
    if 'db' not in g:
        g.db = Db()
    return g.db
