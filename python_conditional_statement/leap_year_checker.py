# Task 1 - Leap Year Checker
year = int(input("Please enter a year: "))

if year % 400 == 0:
    print("This is a leap year")
elif year % 100 == 0:
    print("This is a normal year")
elif year % 4 == 0:
    print("This is a leap year")
else:
    print("This is a normal year")