import random


# Deal Deck Function
def deal_deck(player_1, player_2):
    rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    n = 4
    deck = [item for item in rank for _ in range(n)]
    random.shuffle(deck)

    player_1.extend(deck[0:26])
    player_2.extend(deck[26:52])

    print(f"Player 1: {player_1}")
    print(f"Player 2: {player_2}")


# Play Round Function
def play_round(player_1, player_2):  ## This Function is Wrong - Need to Fix
    card_1 = player_1[0]
    card_2 = player_2[0]

    while card_1 > card_2 or card_1 < card_2:
        player_1.pop(0)
        player_2.pop(0)

    if card_1 > card_2:
        player_1.extend(player_1[0])
        player_1.extend(player_2[0])
    elif card_1 < card_2:
        player_2.extend(player_2[0])
        player_2.extend(player_1[0])
    else:
        ...


# War Case Scenario Function


# Game Loop Function
def play_war(player_1, player_2): ...


def main():
    player_1 = []
    player_2 = []
    deal_deck(player_1, player_2)
    play_round(player_1, player_2)


if __name__ == "__main__":
    main()
