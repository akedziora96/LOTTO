import random


def player_choice():

    """Function takes integers from user (via input) until user types six correct Lotto game lottery numbers.
       Function returns types in form of tuple which contains 6 non repeating integers from 1 to 49"""

    CHOICED_NUMS = []
    i = 1

    while not len(CHOICED_NUMS) == 6:
        try:
            single_choice = int(input(f"Give a #{i} number from 1 to 49: "))
            if single_choice in range(1, 50):
                if single_choice not in CHOICED_NUMS:
                    CHOICED_NUMS.append(single_choice)
                    i += 1
                else:
                    print("You have already chose this number!")
            else:
                print('Number must be in range from 1 to 49!')
                continue
        except ValueError:
            print('Input must be a number!')

    return tuple(sorted(CHOICED_NUMS))


def lotto_game():

    """Function ask player to type 6 lotto numbers ("player_choice" function does it) amd compares it with lottery type
    (6 integers from 1 to 49). Function counts how many player type is the same as lottery type and prints it."""

    RANDOM_NUMS = tuple(sorted([random.randint(1, 49) for i in range(6)]))
    CHOICED_NUMS = player_choice()
    counter = 0

    for num in CHOICED_NUMS:
        if num in RANDOM_NUMS:
            counter += 1

    print(f"Your types: {CHOICED_NUMS}\nLottery types: {RANDOM_NUMS}\nYou hit {counter} lottery balls!")


lotto_game()
