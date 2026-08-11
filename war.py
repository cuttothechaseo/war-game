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
def play_round(player_1, player_2):
    if player_1[0] > player_2[0]:
        player_1.pop()
        player_2.pop()
        player_1.append(player_2[0])
        player_1.append(player_1[0])
    elif player_1[0] < player_2[0]:
        player_1.pop()
        player_2.pop()
        player_2.append(player_1[0])
        player_2.append(player_2[0])
    else:
        ...  # War Case Scenario


# War Case Scenario Function


# Game Loop Function
def play_war(player_1, player_2):
    if len(player_1) == 0:
        print("Game Over - Player 2 Won")
    elif len(player_2) == 0:
        print("Game Over - Player 1 Won")


def main():
    player_1 = []
    player_2 = []
    deal_deck(player_1, player_2)
    play_round(player_1, player_2)
    play_war(player_1, player_2)
    print(len(player_1))
    print(len(player_2))


if __name__ == "__main__":
    main()
