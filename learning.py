def lesson_01_variables():
    name = "Chase"
    age = 28
    learning_python = True

    print(name, age, learning_python)


def lesson_02_strings_and_integers():
    player_1 = "Chase"
    player_1_score = 2
    player_2 = "Bot"
    player_2_score = 1

    print(f"{player_1}, {player_1_score}")
    print(f"{player_2}, {player_2_score}")


def lesson_03_lists():
    drinks = ["Water", "Soda", "Juice", "Beer"]

    print(drinks[0])  # print first item in list
    print(drinks[1])  # print second item in list
    print(drinks[-1])  # print last item in list
    print(drinks[-2])  # print second to last item in list

    drinks.append("Vodka")  # append an item onto an existing list

    print(drinks)


def lesson_04_list_methods():
    cosmetics = ["Toothbrush", "Razor", "Deoderant", "Gel"]
    print(cosmetics)  # initial list
    cosmetics_packed = cosmetics.pop()  # remove last item from list
    print(cosmetics_packed)  # item removed
    print(cosmetics)  # shrunken list
    cosmetics_packed = cosmetics.pop(0)  # remove first item from list
    print(cosmetics_packed)  # item removed
    print(cosmetics)  # shrunken list


def lesson_05_tuples():
    person = ("Chase", 28)
    print(person[0], person[1])

    name, age = person
    print(name)
    print(age)


def main():
    lesson_05_tuples()


if __name__ == "__main__":
    main()
