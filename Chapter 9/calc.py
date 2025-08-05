import math
class calc:
    a = int(input("Number: "))
    square = a*a
    cube = a*a*a
    sqroot1 = math.sqrt(a)
    sqroot2 = round(sqroot1,2)
    def __init__(self):
        print("Hello! Welcome to Square, Cube, and Sq.rt calc!")
        a = self.a
        square = self.square
        cube = self.cube
        sqroot2 = self.sqroot2
        print(f"The square of {a} is {square}\nThe cube of {a} is {cube}\nThe Sqroot of {a} is {sqroot2}")
        print("Thank you!")
    
divyansh = calc()


#OR

import math

class Calc:
    def __init__(self, a):
        print("Welcome to Square, Cube, and Sq.rt calc!")
        self.a = a
        self.square = a * a
        self.cube = a * a * a
        self.sqroot1 = math.sqrt(a) #or a**1/2
        self.sqroot2 = round(self.sqroot1,2)
        print(f"The square of {self.a} is {self.square}")
        print(f"The cube of {self.a} is {self.cube}")
        print(f"The Sqroot of {self.a} is {self.sqroot2}")
        print("Thank you!")

# Taking user input OUTSIDE the class, as is good practice
number = int(input("Number: "))
divyansh = Calc(number)
