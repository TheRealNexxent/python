#input
from operator import itemgetter

input("Name? ")
#Without assigning a variable, the input is wasted.
name = input("Name? ") #This is better.
age = input("Age? ")
print(f"hello, {name}")
print(f"You're {age} years old.")
print("HBD!")
#FStrings for Variables only!
age = int(age)
age = age + 1
print(f"You will be {age} years old after a year!")

#Instead of
#age = int(age)
#age = age + 1
#You can
#int(input) instead, at line six.

#Rect areacalc
l = int(input("Length: "))
b = int(input("Breadth: "))

area = int(l*b)
print(f"The area of this rectangle is {area}.")

#Shopping Cart Prog
item = str(input("What item would you like?: "))
price = float(input("Price of each item?: "))
quantity = int(input("Amount of quantity?: "))

bill = float(price*quantity)
print(f"The total bill for your {item} is {bill} of {quantity} quantity.")
