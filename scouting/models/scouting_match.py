class ScoutingMatch:
    def __init__(self, **kwargs):
        self.team_id = str(kwargs["team_id"])
        self.color = str(kwargs["color"]).upper()
        self.auton_score = int(kwargs["auton_score"])
        self.driver_score = int(kwargs["driver_score"])
        self.tournament_sku = str(kwargs["tournament_sku"])

        # TODO: 2018 competition related scoring

        assert self.color in ["RED", "BLUE"]

    def to_dict(self):
        return {
            "team_id": self.team_id,
            "color": self.color,
            "auton_score": self.auton_score,
            "driver_score": self.driver_score,
            "tournament_sku": self.tournament_sku
        }
