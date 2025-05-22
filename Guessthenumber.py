print("Varun Bellad, 1AY24AI096, Sec-O")
# guessthenumber.py
import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
