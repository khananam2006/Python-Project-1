import random

OPTIONS = ["rock", "paper", "scissors"]

def get_winner(user, comp):
    if user == comp:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "user" if wins[user] == comp else "computer"

def main():
    print("--- Rock Paper Scissors ---")
    while True:
        user = input("Enter rock, paper, or scissors (or 'q' to quit): ").strip().lower()
        if user in ("q", "quit"):
            print("Thanks for playing!")
            break
        if user not in OPTIONS:
            print("Invalid choice. Try again.")
            continue

        comp = random.choice(OPTIONS)
        print(f"Computer chose: {comp}")
        winner = get_winner(user, comp)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win! 🎉")
        else:
            print("Computer wins. 😅")
        print()

if __name__ == '__main__':
    main()