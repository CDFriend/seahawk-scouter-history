class Stats:
    def __init__(self, **kwargs):
        """Team stats for a given event or overall."""
        self.avg_score = int(round(kwargs["avg_score"]))
        self.best_score = int(kwargs["best_score"])
        self.worst_score = int(kwargs["worst_score"])
        self.auton_point_percent = float(kwargs["auton_point_percent"])
