def get_location_str(city, region, country):
    if not (city or region or country):
        return "Unknown"

    return ", ".join([city, region, country])