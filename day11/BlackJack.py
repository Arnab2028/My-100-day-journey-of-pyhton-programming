import random
from art import logo

#---Empty variables----#
user_cards = []
computer_cards = []
computer_score = -1
user_score = -1

def deal_cards():
    """Generates a Random card from the infinite card deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

#---Initial dealing---#
computer_cards.append(deal_cards())
for _ in range(2):
    user_cards.append( deal_cards())

#---Module functions---#
#   I have created 5 functions:-
#   1) Calculate Score,
#   2) Score_display,
#   3) Compare,
#   4) Restart,
#   5) Game_Play
# You can find the functions below: ⬇️

def calculate_score(list):
    """Takes list of cards and returns the score calculated from the list"""
    result = sum(list)
    if result > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    if result == 21 and len(list) == 2:
        result = 0

    return result

def score_display(user_sc, computer_sc):
    """Displays score count"""

    if user_sc == 0:#---BlackJack for user---#
        print(f"---User---\n"
              f"Your cards: {user_cards},  current score: {user_sc + 21}")
        print(f"---Computer---\n"
              f"Computer's first card: {computer_cards}, current score: {computer_sc}")
    elif computer_sc == 0: #---BlackJack for Computer---#
        print(f"---User---\n"
              f"Your cards: {user_cards},  current score: {user_sc}")
        print(f"---Computer---\n"
              f"Computer's first card: {computer_cards}, current score: {computer_sc + 21}")
    else:
        print(f"---User---\n"
              f"Your cards: {user_cards},  current score: {user_sc}")
        print(f"---Computer---\n"
              f"Computer's first card: {computer_cards}, current score: {computer_sc}")


def compare(user, computer):
    """Compares Final scores of the user and the computer"""
    score_display(user, computer)
    print("\n")
    if user == computer:
        print("It is a draw 🥲")
    elif (user == 0) or ((user > computer  and user < 21) or computer > 21):
        if user == 0:
            print("User got black Jack.\n")
        print("😁---User wins---😁")
    elif (computer == 0) or ((computer > user and computer < 21) or user > 21):
        if computer == 0:
            print("computer got black Jack.\n")
        print("😫---computer wins---😫")


def restart():
    """Asks user if they want to restart the game"""
    print("\n" * 2)
    game_restart = input("Type 'R' to restart or type 'E' to exit the game.\n=> ").lower()
    if game_restart == "r":
        print("\n" * 1000)
        game_play()
    elif game_restart == "e":
        print("\n" * 100)
        print("👋---Good bye---👋")
        exit()
    else:
        print("\n" * 50)
        print("⚠️⚠️⚠️---INVALID USER INPUT---⚠️⚠️⚠️")
        restart()


def game_play():
    print(logo)
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        score_display(user_score, computer_score) #---Displays score count---#
        print("\n")

        if (user_score == 0 or computer_score == 0) or user_score > 21:
            compare(user_score, computer_score)
            is_game_over = True
        else:
            user_choice = input("Press 'Y' to take a new card from the deck.\n"
                                "Press 'N' to show the final result.\n=> ").lower()
            if user_choice == "y":
                user_cards.append(deal_cards())

            elif user_choice == "n":
                while computer_score != 0 and computer_score < 17:
                    computer_cards.append(deal_cards())
                    computer_score = calculate_score(computer_cards)

                print("\n")
                compare(user_score, computer_score)
                restart()
            else:
                print("\n" * 50)
                print("⚠️⚠️⚠️---INVALID USER INPUT---⚠️⚠️⚠️\n")
game_play()