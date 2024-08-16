import random

def print_rules():
    print("\n*RULES*:")
    print("ROCK > FIRE, SCISSORS, SPONGE")
    print("PAPER > ROCK, AIR, WATER")
    print("SCISSORS > AIR, PAPER, SPONGE")
    print("FIRE > SCISSORS, SPONGE, PAPER")
    print("WATER > ROCK, SPONGE, SCISSORS")
    print("AIR > WATER, ROCK, FIRE")
    print("SPONGE > WATER, AIR, PAPER")
    print("WARNING: there are 3 rounds in a game")
    print("\nGOOD LUCK!")

def get_user_choice():
    valid_choices = ["rock", "paper", "scissors", "fire", "water", "sponge", "air"]
    while True:
        print("\nChoose one: rock, paper, scissors, fire, water, sponge, air")
        user_choice = input().strip().lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid selection. Please write one: rock, paper, scissors, fire, water, sponge, air")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors", "fire", "water", "sponge", "air"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice in ["fire", "scissors", "sponge"]) or \
         (user_choice == "paper" and computer_choice in ["rock", "air", "water"]) or \
         (user_choice == "scissors" and computer_choice in ["air", "paper", "sponge"]) or \
         (user_choice == "fire" and computer_choice in ["scissors", "sponge", "paper"]) or \
         (user_choice == "water" and computer_choice in ["rock", "sponge", "scissors"]) or \
         (user_choice == "air" and computer_choice in ["water", "rock", "fire"]) or \
         (user_choice == "sponge" and computer_choice in ["water", "air", "paper"]):
        return "user"
    else:
        return "computer"

def play_game():
    print("\nWELCOME TO THE GAME!")
    print_rules()

    while True:
        user_wins = 0
        computer_wins = 0
        draws = 0

        for _ in range(3):  # Her turda 3 kez oynanacak
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"Computer's choice: {computer_choice.capitalize()}")

            result = determine_winner(user_choice, computer_choice)
            if result == "draw":
                print("THIS ROUND IS A DRAW!")
                draws += 1
            elif result == "user":
                print("YOU WIN THIS ROUND!")
                user_wins += 1
            else:
                print("COMPUTER WINS THIS ROUND!")
                computer_wins += 1

        # 3 oyun sonrası toplam sonuc
        print("\nRound Results:")
        print(f"You won {user_wins} times.")
        print(f"Computer won {computer_wins} times.")
        print(f"There were {draws} draws.\n")

        if user_wins > computer_wins:
            print("YOU WIN THE ROUND!")
        elif computer_wins > user_wins:
            print("COMPUTER WINS THE ROUND!")
        else:
            print("THE ROUND IS A DRAW!")

        print("\nDO YOU WANT TO PLAY AGAIN (Y/N)")
        play_again = input().strip().lower()
        if play_again != "y":
            print("GAME OVER, THANK YOU FOR PLAYING!\n")
            break

if __name__ == "__main__":
    play_game()

