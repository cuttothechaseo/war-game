import random

## Setup

# Create list of ticket numbers 1-10
ticket_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Shuffle Randomly
random.shuffle(ticket_numbers)

# Create two empty lists: even_tickets and odd_tickets
even_tickets = []
odd_tickets = []


## Logic


# 4. Write a function


def classify_ticket(number):  # odd/event function looked up on Google
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 5. While loop - I know how to while loops but I am confused here. Calling functions is my weak spot.
while ticket_numbers:
    ticket_drawn = ticket_numbers.pop()

    status = classify_ticket(ticket_drawn)
    print(status)

    if status == "Even":
        even_tickets.append(ticket_drawn)
    else:
        odd_tickets.append(ticket_drawn)


## The display
def show_results(even_tickets, odd_tickets):
    print(even_tickets, odd_tickets)


show_results(even_tickets, odd_tickets)
