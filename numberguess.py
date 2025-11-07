"""Number Guessing Game
Simple CLI game: guess the random number between 1 and 100.
"""
import random


def play():
    low, high = 1, 100
    number = random.randint(low, high)
    attempts = 0
    print(f"I'm thinking of a number between {low} and {high}. Try to guess it!")

    while True:
        try:
            guess = int(input('Enter your guess: ').strip())
        except ValueError:
            print('Please enter a valid integer.')
            continue

        attempts += 1
        if guess == number:
            print(f'Correct! You guessed it in {attempts} attempts.')
            if attempts <= 5:
                print('Nice! Great guessing skills.')
            break
        elif guess < number:
            print('Too low. Try a higher number.')
        else:
            print('Too high. Try a lower number.')


if __name__ == '__main__':
    while True:
        play()
        again = input('Play again? (y/n): ').strip().lower()
        if again not in ('y', 'yes'):
            print('Thanks for playing!')
            break