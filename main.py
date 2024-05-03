import random

def determine_winner(user_input, computer_input):
    # Determine the winner
    if user_input == computer_input:
        return "It's a draw!"
    elif (user_input == "R" and computer_input == "S") or \
         (user_input == "P" and computer_input == "R") or \
         (user_input == "S" and computer_input == "P"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    while True:
        # Get user input
        player_input = input("Rock [R] | Paper [P] | Scissors [S] | Quit [Q]: ").upper()

        # Check if the user wants to quit
        if player_input == "Q":
            print("Thanks for playing!")
            break

        # Validate user input
        if player_input not in ["R", "P", "S"]:
            print("Invalid input. Please enter R, P, S, or Q to quit.")
            continue

        # Convert user input to full name
        if player_input == "R":
            user_choice = "Rock"
        elif player_input == "P":
            user_choice = "Paper"
        else:
            user_choice = "Scissors"

        # Generate computer's choice
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        print(f"Computer chooses {computer_choice}.")

        # Determine the winner and print the result
        print(determine_winner(player_input, computer_choice[0]))

if __name__ == "__main__":
    main()
