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
def start_round(player_1, player_2):
    # Need to add a for or while loop here
    player_1.pop(0)
    player_2.pop(0)

    if player_1[0] > player_2[0]:
        player_1.append(player_2[0])
        player_1.append(player_1[0])
    elif player_1[0] < player_2[0]:
        player_2.append(player_1[0])
        player_2.append(player_2[0])
    else:
        war_round(player_1, player_2)


# War Case Scenario Function
def war_round(player_1, player_2): ...


# Game Loop Function
def play_game(player_1, player_2):
    if len(player_1) > 0 and len(player_2) > 0:
        start_round(player_1, player_2)
    elif len(player_1) == 52:
        print("Game Over - Player 1 Won")
    elif len(player_2) == 52:
        print("Game Over - Player 2 Won")


def main():
    player_1 = []
    player_2 = []
    deal_deck(player_1, player_2)
    start_round(player_1, player_2)
    play_game(player_1, player_2)
    print(f"Player_1: {len(player_1)}")
    print(f"Player_2: {len(player_2)}")


if __name__ == "__main__":
    main()
