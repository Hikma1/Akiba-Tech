secret_num=9
for i in range(1, 6):
    guess=int(input("Guess the number between 1 and 10: "))
    if guess==secret_num:
        print(f"Congratulations! You guessed the correct number at attempt {i}.")
        break
    else:
        print("Sorry, that's not the correct number. Try again.")
else:
    print(f"Sorry, you've used all your attempts. The correct number was {secret_num}.")