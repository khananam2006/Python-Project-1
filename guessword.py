import random

words = ["apple", "banana", "grapes", "mango", "orange"]
word = random.choice(words)
guessed = "_" * len(word)
attempts = 6

print("Guess the fruit name!")
print("Word:", guessed)

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()
    if guess in word:
        guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")
    print("Word:", guessed)

if "_" not in guessed:
    print("You guessed it! 🎉")
else:
    print(f"You lost! The word was '{word}'.")