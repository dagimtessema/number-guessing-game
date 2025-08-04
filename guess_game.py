import random  # Import the random module to generate a random number

# Generate a random number between 1 and 100
random_num = random.randint(1, 100)

# Define the guessing game function
def guess_game():
    # Prompt the user to enter a guess
    user_input = input("Please guess a number between 1 and 100: ")

    # Check if the input is a digit
    if user_input.isdigit():
        guess = int(user_input)  # Convert input to an integer

        # Compare the guess to the random number
        if guess != random_num:
            print("Wrong guess, try again.")
            guess_game()  # Recursively call the function to try again
        else:
            print("🎉 Bingo!")  # Correct guess
    else:
        print("Invalid input. Please enter a number.")
        guess_game()  # Retry if input is not a valid number

# Start the game
guess_game()
