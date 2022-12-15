print("Hello " * 5)
str = "friday"
print("day" in str)
print("fir" in str)

#String Replacement.

age = 24
print("The age is " ,age,".")

#String Formatting.
print("The age is {0}.".format(age))
print("Just testing multiple formatting: {0}, {1}, {2}, {3}, {4}, {5}, and {6}.".format("Sun","Mon","Tue","Wed","Thu","Fri","Sat"))

#Specifying the width.
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}.".format(i, i**2, i**3))

name = "Tim"
age = 24
print(name + f" is {age} years old.")
