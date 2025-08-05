#Python Calculator
Y = "Y"
while Y:
    if Y == "Y":
        print("Welcome to Python Calculator.")
        print("Addition: 1")
        print("Subtraction: 2")
        print("Multiplication: 3")
        print("Division: 4")
        x = int(input("Choose an operation: "))
        if x == 1:
            a1 = int(input("Enter first number: "))
            a2 = int(input("Enter second number: "))
            s1 = a1 + a2
            print("Result: ", s1)
            Y = input("Continue? Y/N ")
        if x == 2:
            a1 = int(input("Enter first number: "))
            a2 = int(input("Enter second number: "))
            s2 = a1 - a2
            print("Result: ", s2)
            Y = input("Continue? Y/N ")
        if x == 3:
            a1 = int(input("Enter first number: "))
            a2 = int(input("Enter second number: "))
            s1 = a1 * a2
            print("Result: ", s1)
            Y = input("Continue? Y/N ")
        if x == 4:
            a1 = int(input("Enter first number: "))
            a2 = int(input("Enter second number: "))
            s1 = a1 / a2
            print("Result: ", s1)
            Y = input("Continue? Y/N ")
        else:
            Y = input("Invalid operation! Retry? Y/N ")
    else:
        break