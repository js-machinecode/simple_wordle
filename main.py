"""
This module contains the main game loop and logic for the Wordle clone.

This is an idiomatic clone of Wordle in Python.
It is a simple command-line game played in the terminal.
The player guesses a five-letter word and has six tries.
After each guess, feedback shows:
- correct letters in the correct position
- correct letters in the wrong position
- incorrect letters
"""

import random


WORDS = [
    "apple",
    "brave",
    "crane",
    "flame",
    "grape",
    "house",
    "knife",
    "lemon",
    "plant",
    "smile",
    "table",
    "tiger",
    "water",
    "zebra",
]


MAX_TRIES = 6
WORD_LENGTH = 5


def choose_word():
    """Return a random word from the word list."""
    return random.choice(WORDS)


def get_guess():
    """Prompt the player until they enter a valid five-letter word."""
    while True:
        guess = input("Enter your guess: ").strip().lower()

        if len(guess) != WORD_LENGTH:
            print("Your guess must be exactly five letters.")
        elif not guess.isalpha():
            print("Your guess must contain only letters.")
        else:
            return guess


def give_feedback(guess, secret_word):
    """
    Return feedback for a guess.

    Uppercase letter = correct letter, correct position
    Lowercase letter = correct letter, wrong position
    _ = incorrect letter
    """
    feedback = []

    for index, letter in enumerate(guess):
        if letter == secret_word[index]:
            feedback.append(letter.upper())
        elif letter in secret_word:
            feedback.append(letter.lower())
        else:
            feedback.append("_")

    return " ".join(feedback)


def play_game():
    """Run the main Wordle game loop."""
    secret_word = choose_word()

    print("Welcome to Python Wordle!")
    print(f"Guess the {WORD_LENGTH}-letter word.")
    print(f"You have {MAX_TRIES} tries.\n")

    for attempt in range(1, MAX_TRIES + 1):
        print(f"Attempt {attempt} of {MAX_TRIES}")
        guess = get_guess()

        if guess == secret_word:
            print(f"\nCorrect! The word was {secret_word.upper()}.")
            print("You win!")
            return

        feedback = give_feedback(guess, secret_word)
        print(f"Feedback: {feedback}\n")

    print("You ran out of tries.")
    print(f"The word was {secret_word.upper()}.")


if __name__ == "__main__":
    play_game()