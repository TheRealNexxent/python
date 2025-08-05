age = int(input("Enter your age: "))


if age%2 == 0:
    print("Even age.")
else:
    print("Odd age.")


if age < 18 and age > 0:
    print("Underage.")
elif age == 18:
    print("Perfect age.")
elif age > 18:
    print("Accepted age.")
elif age > 100:
    print("You are too old.")
else:
    print("Invalid age.")


print("Thank you for using the age checker!")


#Figure out which if is working with elif and else. If can work independently, elif and else are dependent on if.
# If the first if is true, the rest will not be checked.
# If the first if is false, the elif will be checked, and if it is true, the else will not be checked.
# If the first if and elif are false, the else will be executed.

