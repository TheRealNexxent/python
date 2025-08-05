#RECURSION.
#A function that calls itself. Why? Cause its logic is connected to it.
#Let's check Factorial out again.

'''
fact(5) = 5x4x3x2x1
fact(4) = 4x3x2x1
fact(3) = 3x2x1
fact(2) = 2x1
fact(1) = 1

fact(n) = nx(n-1)x(n-1)x....x3x2x1

or

fact(n) = nxfact(n-1)
'''

def fact(n):
    if n ==1 or n == 0:
        return 1 #Cuz fact 0 and 1 is 1 itself.
    return n*fact(n-1)

n = int(input("Enter number: "))
print(f"Factorial: {fact(n)}")


#See? Recursion!
#Saves a lot of lines of code.

def fact1(p):
    factorial = 1
    for i in range(1,p+1):
        factorial *= i
    print(factorial)  # This will also print the factorial of the number entered by the user using a for loop.
fact1(4)
#Longer method.

#Be careful with recursion. Sometimes the stack will keep repeating itself if you make a mistake.
