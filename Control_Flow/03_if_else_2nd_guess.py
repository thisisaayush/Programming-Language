ans = 5

num = int(input("Guess a number:"))

if num == ans:
    print("Your guess is correct: {0}".format(num))

elif num < ans:
    print("Your guess is lower than the answer.")
    num = int(input("Enter your guess again:"))
    if num == ans:
        print("Your guess is correct now:8 {0}".format(num))

else:
    print("Your guess is higher than the answer.")
    num = int(input("Enter your guess again:"))
    if num == ans:
        print("Your guess is correct now: {0}".format(num))

