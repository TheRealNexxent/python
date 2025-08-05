x = int(input("Input number for which you want table: "))
for i in range(1,11):
    print(f"{x}*{i} = {x*i}")

i = 1
while i < 11:
    print(f"{x}*{i} = {x*i}")
    i += 1 #Increment always!


l = ["Lname", "Lnmame2", "divy"]
i = 0
while i < len(l):
    if l[i].startswith("L"):
        print(f"Hi, {l[i]}")
    i += 1 #Through While Loop

for name in l:
    if name.startswith("L"):
        print(f"Hi, {name}!")
        #Through For Loop


y = int(input("Enter a number: "))
for i in range(2,y): #Trick is to set Not Prime condition first. Range is not including 1, and excluding number itself.
    if (y%i) == 0:
        print("Not Prime.")
        break
    else:
        print("Prime.")
        break
i = 1
while i <= y:
    if y == 1:
        print("Unique!")
        break
    elif (y%i) == 0:
        print("Not Prime.")
        break
    else:
        i += 1
        print("Prime.")
        break

#First N Natural Numbers
z = int(input("Enter a number: "))
i = 1
sum = 0
while i <= z:
    sum += i
    i += 1
print(sum)

#Factorial
p = int(input("Enter a number: "))
fact1 = 1
i = 1
while i <= p:
    fact1 *= i
    i += 1
print(fact1)

q = int(input("Number :"))
fact2 = 1
for i in range(1,q+1):

    fact2 *=i
    i +=1
print(fact2)
