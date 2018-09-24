import re
from time import strptime, strftime
from scouting.utils import get_location_str


class Event:
    def __init__(self, **kwargs):
        self.sku = str(kwargs["sku"])
        self.name = str(kwargs["name"])
        self.venue = str(kwargs["loc_venue"])
        self.city = str(kwargs["loc_city"])
        self.region = str(kwargs["loc_region"])
        self.country = str(kwargs["loc_country"])

        # Bit of a hack so strptime can parse the date strings from VexDB.
        # For some reason, time zones in VexDB strings are sent as +HH:MM,
        # rather than +HHMM, the usual format. Uses a regex to make the time
        # zone string from VexDB cooperate with strptime.
        start_time = str(kwargs["start"])
        start_time = re.sub("\+(\d+):(\d+)$", "+\g<1>\g<2>", start_time)
        self.date = strptime(start_time, "%Y-%m-%dT%H:%M:%S%z")

    def get_location_str(self):
        return get_location_str(self.city, self.region, self.country)

    def get_date_str(self):
        return strftime("%B %d, %Y", self.date)
