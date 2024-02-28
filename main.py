# // Import the modules:
import random 
from words import *
from art import *
from stages import *

# // Print the logo art
print(logo)
print()

# // Generate a random word:
random_word = random.choice(word_list)

# //Print the solution to help with debugging
# print(f"The solution is {random_word}")

# Generate "_" for each letter in the word to hide the word
random_word_length = len(random_word)
print()
display = []
for i in range(random_word_length):
    display.append("_")
print(display)
print()

# # // Create a user input for the user's letter and add to a variable
# user_letter = input("Guess a letter for the hidden word:\n").lower()

# // Track whether the game has ended using a boolean in a variable
game_has_ended = False

# // Create lives variable
lives = len(stages)

# // Create a while loop for the game to loop until it is over. Move code for user input to the loop 
while game_has_ended == False:
    # // Create a user input for the user's letter and add to a variable
    user_letter = input("Guess a letter for the hidden word:\n").lower()
    
    # Check whether the user letter has been used already
    if user_letter in display:
        print(f"You have already guessed {user_letter}")
    
    # // Replace the blank in the word with current letter if guessed
    for i in range(random_word_length):
        # // Variable to hold the letter
        letter = random_word[i]
        if letter == user_letter:
            display[i] = letter
    
    print(display)
    # // Create if statement to check if a letter chosen was not in the word, print the art and message with lives left. 
    # // Take one life from lives each time.
    if user_letter not in random_word:
        lives -= 1
        print(f"{user_letter} is not in the word. You lose a life! Lives left = {lives}\n {stages[lives]}")
        
    # // When lives = 0 change the game_has_ended boolean to True and print message to user.
        if lives == 0:
            game_has_ended = True
            print("You lose! Game Over!")
    # // Check whether anymore blanks are in the display word. If not, change the game_has_ended to True, print game message to user.
    if "_" not in display:
        game_has_ended = True
        print("You win! Game Over!")
        
        
        





