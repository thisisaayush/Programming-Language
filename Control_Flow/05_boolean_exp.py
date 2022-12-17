day = input("Enter the day:")
temperature = int(input("Enter the temperature:"))
weather = input("Enter the weather [rainy, windy, sunny]: ")

if (day == "Saturday" and temperature > 27) or not "rainy":
    print("Go Swimming.")

else:
    print("Study Coding.")