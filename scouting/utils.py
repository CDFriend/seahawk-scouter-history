def get_location_str(city, region, country):
    if not (city or region or country):
        return "Unknown"

    vals = []
    if city:
        vals.append(city)
    if region:
        vals.append(region)
    if country:
        vals.append(country)

    return ", ".join(vals)
