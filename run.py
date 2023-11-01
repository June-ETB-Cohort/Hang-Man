import os
import random

from hangman_words import word_list
from hangman_art import stages, logo


def main_menu():
    """
    Displays main menu and returns user's choice.
    """
    clear()
    print(logo)
    print("Welcome to Hangman Game!")
    print("\nMain Menu:")
    print("1. Start a New Game")
    print("2. Game Description")
    print("3. Exit")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        try:
            choice = int(choice)
            if choice > 3 or choice < 1:
                print("Invalid input! Enter your choice (1/2/3): ")
                continue
        except ValueError:
            print("Invalid input! Enter your choice (1/2/3): ")
            continue
        return choice


def game_description():
    clear()
    print(logo)
    print("\nHangman is a word-guessing game where you have"
          " to guess a hidden word letter by letter.")
    print("You can make a limited number of incorrect guesses"
          " before the hangman is complete.")
    print("Your goal is to guess the word before the hangman is fully drawn.")
    print("Good luck!\n")
    input("Press ENTER to continue")


def clear():
    """
    This clears the terminal to prevent clutter on it.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_stage(lives, guesses, message):
    clear()
    print(stages[lives])
    print(f"{' '.join(guesses)}")
    print(message)
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 0:
            print("Guess cannot be empty")
        elif len(guess) > 1:
            print("Guess should not be more than one character!")
        elif not guess.isalpha():
            print("Guess should be a letter")
        else:
            return guess


def main():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    menu_choice = main_menu()
    if menu_choice == 3:
        end_of_game = True
        print("Bye bye!")
        return
    elif menu_choice == 2:
        game_description()
        main()
    else:

        # Testing code
        # print(f'Pssst, the solution is {chosen_word}.')

        # Create blanks
        display = []
        for _ in range(word_length):
            display += "_"

        current_guesses = []
        current_message = ''
        # Starting a main game loop
        while not end_of_game:
            # display_stage(lives, display, '')
            # guess = input("Guess a letter: ").lower()
            guess = display_stage(lives, display, current_message)

            if guess in current_guesses:
                # display_stage(lives, display, f"You've already guessed {guess}")
                current_message = f"You've already guessed {guess}"
            elif guess not in chosen_word:
                # print(f"You guessed {guess}, that's not in the word. You lose a life.")

                lives -= 1
                # display_stage(lives, display, f"You guessed {guess}, that's not in the word. You lose a life.")
                current_message = f"You guessed {guess}, that's not in the word. You lose a life."
                if lives == 0:
                    end_of_game = True
                    # display_stage(lives, display, "You lose.")
                    # current_message = "You lose!"
                    clear()
                    print(stages[lives])
                    print("You are out of lives!")
                    print(f"The word was: {chosen_word}.")
                    print("You lose. Good luck next time!")
            else:

                # Check guessed letter
                for position in range(word_length):
                    letter = chosen_word[position]
                    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                    if letter == guess:
                        # print("GUESS CORRECT!")
                        current_message = "Correct guess!"
                        display[position] = letter

            current_guesses.append(guess)
            # Check if user is wrong.

            # Join all the elements in the list and turn it into a String.
            # print(f"{' '.join(display)}")

            # Check if user has got all letters.
            if "_" not in display:
                end_of_game = True
                clear()
                print(stages[lives])
                print("You got it!")
                print(f"The word was: {chosen_word}.")
                print("You win! Great job!")

        while True:
            play_again = input("Do you want to play again? Y or N: ").lower()
            if play_again not in ["y", "n"]:
                print("Invalid input!")
            elif play_again == 'y':
                main()
            else:
                print("Thank you for playing Hangman. Goodbye!")
                return

            # print(stages[lives])
            # display_stage(lives, display, '')


main()