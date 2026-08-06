def classify_temp(temp):  # classifier function
    if temp >= 80:
        return "Hot"
    elif temp >= 60:
        return "Warm"
    else:
        return "Cool"


def display_place(name, label):
    print(f"{name} - {label}")


def process_temp(places):
    for place in places:
        temp = place["temp"]
        label = classify_temp(temp)
        name = place["area"]

        display_place(name, label)


def main():
    places = [
        {"area": "Houston", "temp": 95},
        {"area": "Chicago", "temp": 70},
        {"area": "New York", "temp": 60},
        {"area": "Utah", "temp": 50},
    ]

    process_temp(places)


if __name__ == "__main__":
    main()
