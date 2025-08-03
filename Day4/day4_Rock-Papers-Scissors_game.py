import random
rock = '''
    _______
---'   ____)
      (_____)
rock  (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
paper     _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
scissors__________)
      (____)
---.__(___)
'''

user_name = input("What is your name?\n=> ")

user = int(input(f"Hello {user_name} welcome to rock, paper, scissors game"
              "press the following options: \n"
              'A) Press "0" to choose rock.\n'
              'B) Press "1" to choose paper\n'
              'C) Press "2" to choose scissors\n'))

game_image = [rock, paper, scissors]
computer = random.randint(0,2)

#---choice---#
if user >= 0 and user <=3:
    print(f"The computer choice {game_image[computer]}")
    print(f"{user_name} choose: {game_image[user]}")

#---Game---#
if user < 0 and user >3:
    print("Try again.\nInvalid input.")
elif computer == 0 and user == 2:
      print("---computer wins---")
elif computer == 2 and user == 1:
      print("---computer wins---")
elif computer == 1 and user == 0:
      print("---computer wins---")
elif computer == user:
      print("---It's a tie---")
else:
      print(f"---{user_name} wins---")


