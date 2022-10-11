import random
from hangman import logo
from hangman import word_list
from hangman import stages
print(logo)
chosen_word=random.choice(word_list) # Randomly choose a word from the word_list and assign it to a variable called chosen_word.
end_of_game=False
lives=6 #variable called 'lives' to keep track of the number of lives left
display=[]
for n in range(0,len(chosen_word)): #Create blanks
    display+='_'
print(display)
while not end_of_game: #while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_")
    guess = input("Guess a letter \n").lower() # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    for n in range(0,len(chosen_word)): #Loop through each position in the chosen_word;If the letter at that position matches 'guess' then reveal that letter in the display at that position.
       if chosen_word[n]==guess:
            display[n]=chosen_word[n]
    display1 = ""
    for n in range(0, len(display)):
           display1 += display[n]
    print(display1)
    if guess not in chosen_word:
        print("the guess letter is not a part of the word. you lose a life") # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives-=1 # If guess is not a letter in the chosen_word, Then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."
        print(stages[lives]) #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    if display1==chosen_word:
        print("You win!")
        exit()
    if lives==0:
        end_of_game=True
        print("You lost!")
        print(f"The word was {chosen_word}")


