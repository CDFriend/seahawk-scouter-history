from scouting.models.scouting_match import ScoutingMatch


class Firebase:
    def get_all_matches(self):
        return [ScoutingMatch(**data) for key, data in self.mock_matches_.items()]

    mock_matches_ = {
        1: {
            "team_name": "9181A",
            "color": "red",
            "auton_score": 5,
            "driver_score": 17,
            "tournament_id": 2912
        },
        2: {
            "team_name": "9181Z",
            "color": "blue",
            "auton_score": 4,
            "driver_score": 12,
            "tournament_id": 2912
        },
        3: {
            "team_name": "1010Q",
            "color": "red",
            "auton_score": 7,
            "driver_score": 15,
            "tournament_id": 2912
        }
    }
