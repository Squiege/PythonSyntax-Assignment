# Task 1 - Identify the greatest
number1 = int(input("Give me a number: "))
number2 = int(input("Give me a number: "))
number3 = int(input("Give me a number: "))

print("The numbers you provided from greatest to smallest are:")

if number1 > number2 and number3:
    if number2 > number3:
        print(number1, number2, number3)
    else:
        print(number1, number3, number2)
elif number2 > number3 and number1:
    if number1 > number3:
        print(number2, number1, number3)
    else:
        print(number2, number3, number1)
else:
    if number1 > number2:
        print(number3, number1, number2)
    else:
        print(number3, number2, number1)

# Task 2 - Identify the Smallest

print("The numbers you provided from smallest to greatest are:")

if number1 < number2 and number3:
    if number2 < number3:
        print(number1, number2, number3)
    else:
        print(number1, number3, number2)
elif number2 < number3 and number1:
    if number1 < number3:
        print(number2, number1, number3)
    else:
        print(number2, number3, number1)
else:
    if number1 < number2:
        print(number3, number1, number2)
    else:
        print(number3, number2, number1)