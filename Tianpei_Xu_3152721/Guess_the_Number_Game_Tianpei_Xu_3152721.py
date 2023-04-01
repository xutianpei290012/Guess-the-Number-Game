import random
import time
import pygame

# Initialize pygame
pygame.init()

# list to store top scores
top_scores = []

# Define sound function
def play_sound(filename):
    # Play a sound effect
    try:
        sound = pygame.mixer.Sound(filename)
        sound.play()
    except:
        pass

# Define high scores function
def show_highest_score():
    # check if there are any scores to display
    if len(top_scores) == 0:
        print("Sry,no scores to display.")
    else:
        # Sorting of scores in ascending order
        top_scores.sort(reverse=False)
        # display the highest score (Minimum number of correct guesses)from the first three games
        if len(top_scores) >= 3:
            print("Minimum number of correct guesses from first three games:", min(top_scores[:]))
        else:
            print("Not enough scores to determine Minimum number of correct guesses from first three games.")
        # display the Ranking of scores
        print("Ranking of scores:")
        for i, score in enumerate(top_scores):
            print(str(i+1) + ". " + str(score) + " guesses")



# Load sound effects
pass_sound = pygame.mixer.Sound("pass.mp3")
fail_sound = pygame.mixer.Sound("fail.mp3")

# Play Gamestart sound effect
play_sound("Gamestart.mp3")
# Display Welcome
print("Welcome to the Number Guessing Game!")

# start the game three times
for i in range(3):
    print("Game", i+1)
    # generate a random number between 1 and 100
    number = random.randint(1, 100)
    # initialize the guess count
    number_of_guesses = 0
    # start the timer
    start_time = time.time()
    # loop until the user guesses the correct number or quits the game
    while True:
        guess = input("Guess a number between 1 and 100(or type 'q' to quit): ")
        # Built to exit the game
        if guess.lower() == "q":
            print("Thanks for playing!")
            break
        try:
            guess = int(guess)
        # Handling other user input
        except:
            print("Unrecognisable input. Please enter a number between 1 and 100.")
            continue
        # increment the guess count
        number_of_guesses += 1
        # if the user has guessed the correct number
        if guess == number:
            # Calculate the clearance time
            elapsed_time = time.time() - start_time
            print(
                f"Congratulations! You guessed the number in {number_of_guesses} guesses and {elapsed_time:.2f} seconds.")
            pass_sound.play()
            # Number of guesses stored
            top_scores.append(number_of_guesses)
            pygame.time.wait(9000)
            break
        # If the guessed figure is less than the actual figure
        elif guess < number:
            print("Your guess is too low!")
            fail_sound.play()
        # If the guessed figure is more than the actual figure
        else:
            print("Your guess is too high!")
            fail_sound.play()


# call the function to show the minimum number of correct guesses from first three games and Ranking of scores
show_highest_score()