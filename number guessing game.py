import random

def number_guessing():
    print("welcome to number guessing game")
    print("guess the number between 1 to 100")

    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != secret_number:
        try:
            guess = int(input("enter the number: "))
            if guess > 100 or guess < 1:
                print("please enter a number from 1 to 100")
                continue
            attempts += 1

            if guess < secret_number:
                print("TOO LOW")
            elif guess > secret_number:
                print("TOO HIGH")
            else:
                print(f"CONGRATULATIONS YOU GUESSED THE NUMBER IN {attempts} ATTEMPTS")

        except ValueError:
            print("INVALID INPUT")



def main():
    play_again = True

    while play_again:
        number_guessing()

        while True:
            response = input("Do you want to play again? (yes/no)").lower()
            if response in ["yes", 'y']:
                play_again = True
                break
            elif response in ["no", 'n']:
                play_again = False
                print("thanks for playing👋")
                break
            else:
                print("please enter yes or no")

if __name__ == "__main__":
    main()

