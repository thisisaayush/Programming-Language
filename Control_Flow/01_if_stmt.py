name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Your are eligible to vote.")

else:
    print("You will be eligible to vote in {0} years".format(18 - age))