# Check if the input is a digit
    if user_input.isdigit():
        guess = int(user_input)  # Convert input to an integer

     # Initiate a while loop that runs until a break statement is executed
        while True:
        # Compare the guess to the random number
            if guess == random_num: # Check if guess matches random number
                print("🎉 Bingo!") # Congratulate user on correct guess
                break # Exit the while loop and end the game as user has won
            # If guess is incorrect proceed to the next condition
            elif guess<random_num: # check if guess is lower than the random number
                print("Wrong guess, try higher.") # Give hint
                user_input = input("Please guess a number between 1 and 100: ") # Prompt the user to enter a guess
                if user_input.isdigit():
                    guess = int(user_input) # update guess with new value and go back to condition 1 of while loop
                else:
                    print("Invalid input. Please enter a number.")
                    break # if input is not a number exit the loop and end the game
            elif guess>random_num: # Check if guess is higher than the random number
                print("Wrong guess, try lower.")
                user_input = input("Please guess a number between 1 and 100: ")
                if user_input.isdigit():
                    guess = int(user_input)
                else:
                    print("Invalid input. Please enter a number.")
                    break
    else:
        print("Invalid input. Please enter a number.")
        guess_game()  # Retry if input is not a valid number

# Start the game
guess_game()

