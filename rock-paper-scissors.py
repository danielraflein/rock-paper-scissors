import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
RPS = [rock, paper, scissors]
randomChoice = random.randint(1, 3)
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose!")
    exit()
else:
    pass

selectedBot = RPS[randomChoice - 1]
selectedUser = RPS[userChoice]

print(f"{selectedUser}\nComputer chose:\n{selectedBot}")

# USER
if selectedUser == selectedBot:
    print("It's a draw")
elif selectedUser == rock and selectedBot == scissors:
    print("You win")
elif selectedUser == scissors and selectedBot == paper:
    print("You win")
elif selectedUser == paper and selectedBot == rock:
    print("You win")
# BOT
elif selectedBot == rock and selectedUser == scissors:
    print("You Lose")
elif selectedBot == scissors and selectedUser == paper:
    print("You Lose")
elif selectedBot == paper and selectedUser == rock:
    print("You Lose")