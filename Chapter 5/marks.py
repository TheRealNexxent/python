import time
marks = []
m1 = int(input("Enter your marks: "))
time.sleep(1)
print("Accepted.")
time.sleep(1)
m2 = int(input("Enter your marks: "))
time.sleep(1)
print("Accepted.")
time.sleep(1)
m3 = int(input("Enter your marks: "))
time.sleep(1)
print("Accepted.")
time.sleep(1)
marks.append(m1)
marks.append(m2)
marks.append(m3)

print(f"Your total marks are {marks}, out of 100 each.")
time.sleep(1)
print("The requirement is a totality of 40% to pass, with 33% within each subject.")
time.sleep(1)
print("Checking...")
time.sleep(1)
print("...")

if ((marks[0] + marks[1] + marks[2])/300)*100 >= 40 and marks[0] >= 33 and marks[1] >= 33 and marks[2] >= 33:
    print("Congratulations! You have passed.")
else:
    print("Sorry, you have failed. Please try again.")