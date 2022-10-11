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

choices=(rock,paper,scissors)
computer_choice=random.randint(0,2)
user_choice=int(input("Enter 0 for rock 1 for paper 2 for scissor\n"))
print(f"User choice: \n{choices[user_choice]}")
print(f"Computer choice:\n {choices[computer_choice]}")
if user_choice==0:
    if computer_choice==0:
        print("Tie")
    if computer_choice==1:
        print("Computer wins")
    if computer_choice==2:
        print("You win")
if user_choice==1:
    if computer_choice==0:
        print("You win")
    if computer_choice==1:
        print("Tie")
    if computer_choice==2:
        print("Computer wins")
if user_choice==2:
    if computer_choice==0:
        print("Computer wins")
    if computer_choice==1:
        print("You win")
    if computer_choice==2:
        print("Tie")


