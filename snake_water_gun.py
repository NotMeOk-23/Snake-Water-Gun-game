import random as rn

'''
1 for snake
-1 for water
0 for gun
'''

def get_computer_choice():
    """Returns a random choice for the computer."""
    return rn.choice([1, 0, -1])

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner.
    Returns:
    - 1 if user wins
    - -1 if user loses
    - 0 if draw
    """
    if computer_choice == user_choice:
        return 0

    # User wins: Snake (1) beats Water (-1), Water (-1) beats Gun (0), Gun (0) beats Snake (1)
    if (user_choice == 1 and computer_choice == -1) or \
       (user_choice == -1 and computer_choice == 0) or \
       (user_choice == 0 and computer_choice == 1):
        return 1

    return -1

def main():
    computer = get_computer_choice()
    youstr = input("Enter your choice (s/w/g): ")
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    try:
        you = youDict[youstr.lower()]
    except KeyError:
        print("Invalid choice! Please enter s, w, or g.")
        return

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    result = determine_winner(you, computer)

    if result == 0:
        print("It's a draw!")
    elif result == 1:
        print("You won!")
    else:
        print("You lost!")

if __name__ == "__main__":
    main()
