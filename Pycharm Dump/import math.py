import math
x = 9.9
print(math.pi)
print(math.e) #Exponential Constant.
result = math.sqrt(x)
result2 = math.floor(x) #or ceil.
print(result)
print(result2)

#Circumference of a circle
radius = float(input("Radius? "))
circumference = 2 * math.pi * radius
print(f"The circumference is {round(circumference, 4)}cm.")  #SYNTAX: round(value, number of digits)

#Area of a circle
radius = float(input("Radius? "))
area = math.pi * radius ** 2
print(f"The area is {round(area, 4)}.")

#Hypotenuse of RIGHT ANGLE TRIANGLE: c^2 = a^2+b^2
a = int(input("Side A: "))
b = int(input("Side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"side c is {c}")