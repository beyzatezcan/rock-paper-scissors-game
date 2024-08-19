import random

def tas_kagit_makas_BEYZANUR_TEZCAN():
    def print_rules():
        print("\n\tRULES")
        print("ROCK > FIRE, SCISSORS, SPONGE")
        print("PAPER > ROCK, AIR, WATER")
        print("SCISSORS > AIR, PAPER, SPONGE")
        print("FIRE > SCISSORS, SPONGE, PAPER")
        print("WATER > ROCK, SPONGE, SCISSORS")
        print("AIR > WATER, ROCK, FIRE")
        print("SPONGE > WATER, AIR, PAPER\n")
        print("WARNING: The game continues until one side wins two rounds.\nif you want to exit, you can press the 'x' key.")
        print("\nGOOD LUCK!")

    def get_user_choice():
        valid_choices = ["rock", "paper", "scissors", "fire", "water", "sponge", "air"]
        while True:
            print("\nChoose one: rock, paper, scissors, fire, water, sponge, air")
            user_choice = input().strip().lower() # strip ve lower fonk ile case sensitivity ortadan kalkar
            if user_choice == 'x':
                print("You chose to exit the game.")
                return None
            elif user_choice in valid_choices:
                return user_choice
            else:
                print("Invalid selection. Please choose from: rock, paper, scissors, fire, water, sponge, air")

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

            while user_wins < 2 and computer_wins < 2:  # Oyun iki tur kazanan olana kadar devam eder
                user_choice = get_user_choice()
                if user_choice is None:  # kullanici oyundan cikmak istedi ve none dondu cikis yapildi
                 return
                computer_choice = get_computer_choice()

                print(f"Your choice: {user_choice}")
                print(f"Computer's choice: {computer_choice}")

                result = determine_winner(user_choice, computer_choice)
                if result == "draw":  
                    print("THIS ROUND ENDED IN A DRAW!") # draw yani beraberlik durumunda counter kullanmiyorum cunku oyun algoritmasi kazanmak uzerine
                elif result == "user":
                    print("YOU HAVE WON THIS ROUND!")
                    user_wins += 1
                else:
                    print("COMPUTER HAS WON THIS ROUND!")
                    computer_wins += 1

                # round sonucunu gosterir
                print(f"\nCurrent score: You {user_wins} - {computer_wins} Computer\n")

            # oyun sonucunu gosterir
            if user_wins > computer_wins:
                print("YOU WON THE GAME!")
            else:
                print("COMPUTER WON THE GAME!")

            print("\nDO YOU WANT TO PLAY AGAIN (Y/N)?")
            user_decision = input().strip().lower()
            
            # bilgisayarin tekrar oynamak isteyip istemediğini random ile belirliyoruz
            computer_decision = random.choice(["y", "n"])
            print(f"Computer wants to play again: {computer_decision.upper()}")

            # iki taraf da oynamak istiyorsa dongu devam eder, aksi halde oyun biter
            if user_decision == "y" and computer_decision == "y":
                print("Starting a new game...\n")
                continue  # yeni oyuna başlar
            else:
                print("GAME OVER, THANK YOU FOR PLAYING!\n")
                break  # oyun sona erer

    play_game() # oyunun tekrar baslamasini bu fonk ile sagliyoruz kullanmazsak oyun tek seferlik olur

if __name__ == "__main__":
    tas_kagit_makas_BEYZANUR_TEZCAN()
