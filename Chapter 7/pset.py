#Greatest of 3 nos Fucntion

def gst(x, y, z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    elif z>x and z>y:
        print(z)
    else:
        print("Same values!")

gst(9,9,8)

#Celsius to Farhenheit.

def tempconv(c):
    x = (c*(9/5)) + 32
    print(round(x,2)) #Round function to keep it clean. round(val,decimanptamt)

tempconv(3)

#To prevent python func to print new line at end.
def notnewlineprint(text):
    print(text, end=" ")
    print("New Line did not form!")

notnewlineprint("Hello!")

#Function for First n lines of this:
'''
***
**
*
'''
def star(n):
    for i in range(1,n+1):
        print("*"*n)
        n -= 1

star(3)

#Function for First n lines of this:
'''
***
**
*
'''
#VIA RECURSION

def star(x):
    if (x==0):
        return #Basically like break. It stops the function call here.
    print("*"*x)
    star(x-1)

star(3)


#Inch to cm

def cm(o):
    p = o*2.54
    return p
o = int(input("Enter val: "))
print(cm(o))

#Remove a word from list, and strip it at the same time.
def lis(word):
    print(word.strip())
    x = []
    x.append(word)
    print(x)
    x.pop()
    print(f"The string has been popped from the list. The final list is: {x}")
lis("   Div   yansh   ")

#Alternative method.
def rem(l, word):
    l.remove(word)
    return l
l = ["aaaaaan","baaan","can"]

def rem2(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n #Basically creates a new list for the stripped elements since you cannot change it directly through the list.
print(rem2(l,"an")) #Strip removes ALL THE OCCURENCES OF THE CHARACTERS MENTIONED, NOT ORDERED

#Mul table Function
def mul(x):
    for i in range(1,11):
        print(f"{x}*{i} = {x*i}")
        i += 1
mul(2)


#First n natural numbers using recursion function.

'''
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
sum(n) = 1+2+3....+n
sum(n) = sum(n-1) + n
'''

def sumn(n):
    if n==1:
        return 1 #We did this cause,  it might repeat itself infinitely and give error of repeating itself 996 times like the error before. 
        #Basically if its going backwards, then if there is no n==1, it will go 0+1, 0+1, 0+1, endlessly!
    return sumn(n-1) + n

print(sumn(4))

