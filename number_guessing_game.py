import random

print("=" * 35)
print("      NUMBER GUESSING GAME")
print("=" * 35)

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.\n")
        elif guess > secret_number:
            print("Too high! Try again.\n")
        else:
            print("\n🎉 Congratulations!")
            print(f"You guessed the correct number in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.\n")