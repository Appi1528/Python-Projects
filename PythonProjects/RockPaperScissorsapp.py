import random

print(" Welcome to Rock, Paper, Scissors Game!")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    print("\nChoose: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print(" It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # Display Scores
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

    # Play Again Option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break
