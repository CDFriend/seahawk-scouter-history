class Team:
    def __init__(self, **kwargs):
        if kwargs["size"] <= 0:
            raise CouldNotFindError()
        result = kwargs["result"][0]

        self.id            = str(result["number"])
        self.program       = str(result["program"])
        self.team_name     = str(result["team_name"])
        self.robot_name    = str(result["robot_name"])
        self.organisation  = str(result["organisation"])
        self.city          = str(result["city"])
        self.region        = str(result["region"])
        self.country       = str(result["country"])
        self.grade         = str(result["grade"])
        self.is_registered = bool(result["is_registered"])

    def get_location_str(self):
        if not (self.city or self.region or self.country):
            return "Unknown"

        return ", ".join([self.city, self.region, self.country])
