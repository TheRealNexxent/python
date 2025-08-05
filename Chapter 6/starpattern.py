#Star Pattern for n = 3
# '''
#   *
#  ***
# *****
# '''

n = 3
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end = "") #Adding End for keeping on same line, and not moving to new.
    print("") #For New line. No need to put \n else it will make 2 line gap.

# #Star Pattern for n = 3
# '''
# *
# **
# ***
# '''

o = 3
for i in range(1, n+1):
    print("*"*i, end="")
    print("")

# #Star Pattern for n = 3
# '''
# ***
# * *
# ***
# '''
n = 3
for i in range(1,n+1):
    if i == 1 or i == n:
        print("*"*n, end = "")
    else:
        print("*", end = "")
        print(" "*(n-2), end = "")
        print("*", end = "")
    print("")

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1) or (j == 0 or j == n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to the next line after each row.


#To reverse the multiplication table:
n = int(input("Number: "))
for i in range(1,11):
    print(f"{n}*{11-i} = {n*(11-i)}") #n+1 - i

'''
1 10 --> n+1 - i
2 9
3 8
4 7
5 6
6 5
7 4
8 3
9 2
10 1
'''
