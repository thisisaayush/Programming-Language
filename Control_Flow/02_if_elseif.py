ans = 5

num = int(input("Enter your guess number:"))

if num == ans:
    print("Your guess is correct: {0}".format(ans))

elif num < ans:
    print("Your guess is lower than the answer.")

else:
    print("Your guess is higher than the answer.")