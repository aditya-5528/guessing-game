number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("guess your number"))
    guess_count += 1
    if guess == number:
        print("you won")
        break
else:
    print("you lose")
