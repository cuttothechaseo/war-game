# How Multiple Functions Connect Together

# Pass 1
def classify_temp(temp):  # classifier function
    if temp >= 80:
        return "Hot"
    elif temp >= 60:
        return "Warm"
    else:
        return "Cool"

def display_temp(temp): # display function
    ## mind is drawing a blank - what do I do here

def process_temp(temp): # process function
    label = # idk what comes next
    print(f"{temp}['area'] - {label}")

def (): # I think this is the loop function
    for place in places:
        return display_temp(temp)

def(): # This is where the dictionary goes
    places = [
        {"area": "Houston", "temp": 80},
        {"area": "Washington", "temp": 60},
        {"area": "San Antonio", "temp": 90},
        {"area": "New York", "temp": 50},
    ]

    # this is where we call the loop function maybe?

# Pass 2
def classify_temp(temp): # Classify Function
    if temp >= 90:
        return "Hot"
    elif temp >= 70:
        return "Warm"
    else:
        return "Cool"

def display_temp(places, label): # Display Function - I want to display the area and the temp in an f-string
    label = {places['area']}
    print(f"{place['area']} - {label}")

def process_temp(places): # For Loop - Run through the below dictionary
    for place in places:
        display_temp(places)

# Pass 3
def classify_temp(temp): # Classify Function
    if temp >= 80:
        return "Hot"
    elif temp >= 65:
        return "Warm"
    else:
        return "Cool"

def display_temp(place, temp): # My thought process here is I want to print a dictionary from the future list and tag it to the temp label. the label == the above classify function.
    print(f"{place['area']} - {label}") # Print each dictionaries 
    label = classify_temp(temp)

def process_temp(places): # loop function to print entire list
    for place in places: # for loop
        display_temp(place) # loop through the above display function

    places = [
        {"area": "Houston", "temp": 90},
        {"area": "Greenland", "temp": 40},
        {"area": "New York", "temp": 70},
        {"area": "San Antonio", "temp": 80},
    ]

    display_temp()

# Pass 4

def classify_temp(temp):
    if temp >= 80:
        return "Hot"
    elif temp >= 65:
        return "Warm"
    else:
        return "Cool"

def display_temp(place, label): # This is where I get stuck. What arguments should go after display_temp? It's hard for me to grasp since I haven't written the dictionary yet
    label = classify_temp() # Can't really wrap my head around this. Should the label just be the above classify function?
    print(f"{place['area']} - {label}") # So I want to say print the place's area and the corresponding temp according to the classify function

def process_temp(temp): # what argument should go in this line? Is it the temp? Can't wrap my head around
    for place in places:
        # Idk what should go here. You mentioned I call the classify function. Why wouldn't I call the display function since that's what I want it to loop?

def main(): # So this is the function where I write the dictionary
    places = [
        {"area": "Houston", "temp": 90},
        {"area": "Greenland", "temp": 40},
        {"area": "New York", "temp": 70},
        {"area": "San Antonio", "temp": 80},
    ]

    display_temp() # I think this is what I want to return? The f-string.