#To make a copy of file.
#Pset Q8

f = open("this.txt")
x = f.readlines()
y = "".join(x) #Or directly write f.read() and save yourself the effort to convert to string.
print(x)
print(y)
g = open("thiscopy.txt", "w")
g.write(y)
f.close()
g.close()

#Furthermore lets check if the items are identical
#Pset Q9

f.open("this.txt")
g.open("thiscopy.txt")
if f.readlines() == g.readlines(): #OR f.read and g.read
    print("Identical!")
else:
    print("Not Identical.")
f.close()
g.close()

#Now lets wipeout the content.
#Pset Q10

f = open("this.txt", "w")
f.write("")
f.close()

