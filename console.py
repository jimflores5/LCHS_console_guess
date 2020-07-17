import random
    
def input_guess(start, end):
    valid_input = False
    while not valid_input:
        user_input = input("Guess a number between {0} and {1}:\n".format(start, end))
        try:
            user_input = int(user_input)
            if user_input >= start and user_input <=end:
                valid_input = True
        except:
            print("Enter a whole number!")
    
    return user_input

def main():
    still_playing = True
    while still_playing:
        start_value = random.randint(0, 20)
        end_value = random.randint(30, 100)
        magic_number = random.randint(start_value, end_value)

        still_guessing = True
        num_guesses = 0
        print("Welcome to the Guessing Game!\n")

        while still_guessing:
            guess = input_guess(start_value, end_value)
            num_guesses += 1

            if guess == magic_number:
                print("CORRECT!")
                print(f"You took {num_guesses} tries to guess the number.")
                still_guessing = False
            elif guess < magic_number:
                print(f"Sorry, {guess} is too low.")
                start_value = guess
            else:
                print(f"Sorry, {guess} is too high.")
                end_value = guess

        replay = input("Would you like to play again (Y/N)? ")
        if replay[0].lower() != 'y':
            still_playing = False

    print("Thanks for playing!")

if __name__ == '__main__':
    main()