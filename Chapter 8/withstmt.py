f = open("file.txt")
print(f.read())
f.close()

#The same can be written via with statement like so:

with open("file.txt") as f:
    print(f.read())

    
#You dont have to explicitly clsoe the file if you do this! With eliminates the same. As soon as you are outside the statement, it closes. Like right now. its closed.

