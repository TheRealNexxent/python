#To mine a file and check if it has Python in it.

f = open("pythonf.txt")
x = f.readlines()
print(x)
y = "".join(x)
print(y)
if "python" in y.lower():
    print("Yes")
else:
    print("No")
f.close()
f = open("pythonf.txt")
z=1
while z>0:
    if "python" in f.readline():
            print(f"The line on which Python exists is Line: {z}")
            break #IF YOU BREAK HERE, THEN ELSE WONT RUN!
    else:
        z += 1 #Better for readability, but you can also write:
# while z>0:
#     if "python" in f.readline():
#             print(f"The line on which Python exists is Line: {z}")
#             break
#     z += 1 ---> You dont have to mention Else explicitly.
    

            #DONE
#Lorem435 in HTML file generates a huge string. useful for this code to try on large set.