#Class Train to do ticket booking status getting number of seats and fare information.

class train:
    name = str
    age = int
    no_seats = int
    def __init__(self, name, age, no_seats):
        print("Welcome to train booking system.")
        print("Press 1 for booking")
        print("Press 2 for Number of seats available")
        print("Press 3 for ticket fare information")



ch = int(input("Choice? "))
if ch == 1:
    name = input("Name? ")
    age = int(input("Age? "))
    no_seats = int(input("How many Seats? "))
    option1 = train(name, age, no_seats)
    print(option1.name)