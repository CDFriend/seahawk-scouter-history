from scouting.utils import get_location_str


class Event:
    def __init__(self, **kwargs):
        self.sku = str(kwargs["sku"])
        self.name = str(kwargs["name"])
        self.venue = str(kwargs["loc_venue"])
        self.city = str(kwargs["loc_city"])
        self.region = str(kwargs["loc_region"])
        self.country = str(kwargs["loc_country"])

        # TODO: parse date

    def get_location_str(self):
        return get_location_str(self.city, self.region, self.country)
