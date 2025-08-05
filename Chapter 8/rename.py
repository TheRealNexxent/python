import os
f = open("old.txt")
x = f.read()
print(x)
f.close()

g = open("new.txt", "w")
y = g.write(x)
g.close()

os.remove("old.txt") #To remove a file as well, just for decorative purposes.