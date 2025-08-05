#Strings
first_name = "Divyansh"
food = "burger"
email = "divy123@breh.com"
print(first_name)
#or`
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#Integers
age = 25
quantity = 3
student_count = 30
print(f"You are {age} years old")
print(f"You have bought {quantity} of {food}")
print(f"Your class of {student_count} has bought {quantity} of {food} each")

#Float
price = 99.9
gpa = 3.2
distance = 5.5
print(f"Your price is {price} for {quantity} of {food}")
print(f"Your gpa is {gpa}")
print(f"Your destination is {distance} kilometers away")

#Boolean
is_student = False
for_sale = True
is_online = False
print(f"Are you a student? {is_student}")
if is_student:
    print(f"{is_student} You are a student.")
else:
    print("You are not a student")

if for_sale:
    print("Available to buy.")
else:
    print("Sorry, out of stock!")

if is_online:
    print("You're online!")
else:
    print("You're offline!")

#Typecasting
value = 10
gpaa = 2.3
is_student = False

print(type(gpaa))

gpaa = int(gpaa)
print(gpaa)
is_student = int(is_student)
print(is_student)
is_online = float(is_online)
print(is_online)
is_offline = str("is_offline")
print(is_offline)
gpaa = bool(gpaa)
print(gpaa)

age = str(age)
age += "1"
print(age)

#In case of string to boolean, if string is empty then false, else always true.




