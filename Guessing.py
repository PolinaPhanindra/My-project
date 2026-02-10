import random
secret_number = random.randint(1, 100)
attempts = 0
while True:
    guess_num=int(input("Enter the number between 0 to 100: "))
    attempts +=1
    if secret_number == guess_num:
        print(f"YaY!! correct you guessed the number in {attempts} attempts")
        break
    elif guess_num > secret_number :
        print("Guess is too high, try again")
    else:
        print("Guess is too low, try again")
print(f"Screte number is: {secret_number}")