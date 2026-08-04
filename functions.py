def get_temp(temp):
    if temp >= 80:
        return "Hot"
    elif temp >= 65:
        return "Warm"
    else:
        return "cold"


places = [
    {"area": "Norway", "temp": 20},
    {"area": "Miami", "temp": 80},
    {"area": "Ireland", "temp": 50},
]

for place in places:
    label = get_temp(place["temp"])
    print(f"{place['temp']} - {label}")
