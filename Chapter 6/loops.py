for i in range(1,1001):
    print(i)
#1001 cuz range is exclusive of the last number.

# While loop
i = 1
while i < 6:
    print(i)
    i += 1  # Increment i to avoid infinite loop.
# This will print numbers from 1 to 5, but you can change it to = for including 6.

# l1 = [1,2,3,4, "divy", True, 2.3]
# i = 1
# while l1[i] in l1 and i< len(l1):
#     print(l1[i])
#     i += 1  # Increment i to avoid infinite loop.
# The condition l1[i] in l1 will always be true for valid indices, so the loop never stops on its own and will eventually crash with an IndexError.
#instead do this:
l1 = [1, 2, 3, 4, "divy", True, 2.3]
i = 0
while i < len(l1):
    print(l1[i])
    i += 1  # Increment i to avoid infinite loop.
# This will print each elem
# ent in the list l1 until it reaches the end of the list. and Index will go from 0-6, so it stays lesser than 7, and prints all elements.


# For Loop.

for i in range(1,100,5):
    print(i)

list2 = [1, 2, 3, 4, "divy", True, 2.3]
for i in list2:
    print(i)

t = (6, 25, 30)
for i in t:
    print(i)
else:
    print("This is the end of the tuple") #For loop with Else. Printed when LOOP EXHAUSTS.

d = {"name": "Divy", "age": 20, "isStudent": True}
for key in d:
    print(key, ":", d[key])
else:
    print("This is the end of the dictionary")

s = {1,2,3,45}
for i in s:
    print(i)
else:
    print("This is the end of the set")

str = "Divy"    
for i in str:
    print(i)
else:
    print("This is the end of the string")

for i in range(1,100):
    if i == 34:
        break
    print(i)
print("Broke!")  # This will print when the loop is broken by the break statement.

for i in range(1,100):
    if i == 34:
        continue
    print(i)
#Skips the number 34 and continues with the next iteration of the loop, as in yg the loop will never be 34, it will skip it and continue with the next number. it doesnt start from zero agian
#It's basically skip.
for i in range(1,100):
    pass #For working on this code later, it does nothing but is syntactically correct.
# The pass statement is a null operation; nothing happens when it executes. It's useful as a placeholder in loops, functions, classes, or conditionals where you plan to add code later but want to keep the structure intact.
i = 0
for i in range(1,200):
    print(i)

x = int(input("Enter a number: "))
for i in range(1,11):
    print(x*i)
    i += 1

y = int(input("Enter another number: "))
i = 0 #For while you have to set the initial value of i before the loop.
while i < 11:
    print(y*i)
    i += 1

l = ["Harry", "Rohan", "Hammad", "Divy"]
for i in l:
    if i.startswith("H"):
        print(f"Hello, {i}!")
3
x = int(input("Number: "))
for i in range(2,x):
    if (x%i) == 0:
        print("Not Prime")
        break
else:
    print("Prime") #Keep outside for loop for final check, if the loop exhausts without finding a factor, it will print "Prime". Also if inside loop, then range is 2,2 so loop never even runs for 2.


n = int(input("Enter a number: "))
i = 1
sum = 0
for i in range(1,n+1):
    sum += i
    i += 1

print(sum) #Keep sum first, then increment i else you are adding an incremented value to the sum, which is not what you want. You want to add the original value of i x to the sum.

o = int(input("Enter a number: "))
i = 1
factorial = 1
while i <= o:
    factorial *= i
    i += 1
print(factorial)  # This will print the factorial of the number entered by the user.

p = int(input("Enter another number: "))
factorial = 1
for i in range(1,p+1):
    factorial *= i
print(factorial)  # This will also print the factorial of the number entered by the user using a for loop.

f1 = int(input("Enter number: "))
fact = 16

for i in range(1, f1 + 1):
    fact *= i
print(fact)  # This will print the factorial of the number entered by the user using a for loop.

# ***
# * *
# ***
n = 3

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1) or (j == 0 or j == n - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()  # Move to the next line after each row.