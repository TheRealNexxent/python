f = open("file.txt", "r")
lines = f.readlines() #Reads all lines
line = f.readline() #Note. If you use readline after running readlines, it will return nothing, since the pointer has read all the lines and is now at the end of line, so has nothing to read.
l1 = f.readline()
l2 = f.readline()
l3 = f.readline()
l4 = f.readline()
l5 = f.readline() #Reads lines individually.
print(l1)
print(type(l1))
print(l2)
print(type(l2))
print(l3)
print(type(l3))
print(l4)
print(type(l4))
print(l5)
print(type(l5)) #Prints nothing. Empty line, and default str type.
while (line != ""): #To create a loop for the same, since above process looks cubersome!
    print(line)
    line = f.readline()

#Prints Line by line in form of list.
f.close()
