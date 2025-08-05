import time
numberlist = []
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))
numberlist.append(n1)
numberlist.append(n2)
numberlist.append(n3)
numberlist.append(n4)
print(numberlist)
time.sleep(2)
if numberlist[0] > numberlist[1] and numberlist[0] > numberlist[2] and numberlist[0] > numberlist[3]:
    print("The greatest number is: ", numberlist[0])
    time.sleep(2)
elif numberlist[1] > numberlist[0] and numberlist[1] > numberlist[2] and numberlist[1] > numberlist[3]:
    print("The greatest number is: ", numberlist[1])
    time.sleep(2)
elif numberlist[2] > numberlist[0] and numberlist[2] > numberlist[1] and numberlist[2] > numberlist[3]:
    print("The greatest number is: ", numberlist[2])
    time.sleep(2)
elif numberlist[3] > numberlist[0] and numberlist[3] > numberlist[1] and numberlist[3] > numberlist[2]:
    print("The greatest number is: ", numberlist[3])
    time.sleep(2)
else:
    print("There is no greatest number, all numbers are equal.")
    time.sleep(2)

print("Thank you for using the greatest number checker!")