from scouting.db import Db
from scouting.models.scouting_match import ScoutingMatch
from scouting.models.transaction import ScoutingTransaction

dummy_match = ScoutingMatch(
    team_id="9181A",
    color="RED",
    auton_score=12,
    driver_score=15,
    tournament_sku="EVENTSKU"
)


def test_commit_transaction():
    db = Db()
    trans = ScoutingTransaction()
    trans.add_match(dummy_match)

    matches_init = len(db.get_all_matches())
    db.commit_transaction(trans)
    matches_end = len(db.get_all_matches())

    assert matches_end - matches_init == 1
