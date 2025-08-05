def calc():
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
calc()

def greet():
    name = input("Name: ")
    print(f"G'day, {name}!")
    print("Hello, " + name)

#orr

def greet(Name):
    print(f"Gday, {Name}")
greet("Divy")

#Name is a parameter.
#You can have multiple parameters.

#also

def x(z):
    y = print("7")
    gr = "Hello " + z
    return gr #Return for using when u wanna assign a variable to this function and not get "None" when you print it.

p = x("Divy") #Function call, will return Hello Divy
print(p)

def goodDay(name, ending = "Thank you"): #Here, if ending was not assigned anything, then it would return error since value has not been supplied. if you dont use ending also its fine here!
    print("Gday!", name)
    print(ending)
goodDay("Nex")
#If ending value is not supplied at line 3, but assigned above, then by default it will assign and do nothing error.
goodDay("Harry", "Thanks")
#Here, since we changed ending variable value, it prints Godo day Harry Thanks! See what i mean?

