#Remove Donkey and replace with ######
words = ["sab", "kuch", "Donkey"]

f = open("donkey.txt")
x = f.read() #Better to retrieve a string directly and not have to worry about any other operations.
# print(x)
# print(type(x))
# x = f.readlines()
# print(x)
# print(type(x))
z = "".join(x)
print(z)
print(type(z))

q = z.lower()

print(q)
for word in words:
    x = x.replace(word, "#"*len(word))
    print(x)

f.close()
f = open("donkey.txt", "w")
f.write(x)
f.close()

#SOLVED!
#Even if you close the file prior, it doesnt mean the variables and the operations within that open file wont carry over to the next iteration!
#Try reading through the comment lines. That was your first iteration without using read. It was impressive!
#Because you had to readlines list --> string first and then read it all and convert.
#Im not deleting it cause it was difficult, and you STILL made it work.
#long route, but good concepts!
'''
NOTE!
Even though you close the file object f after reading, the variables you created (x, z, q, etc.) still exist in memory and carry their current values.

Closing the file means:

The file descriptor is released,

The file is no longer accessible through that f object,

But variables remain unchanged and can still be used, assigned, and manipulated.

So, all your string operations (z.lower(), z.replace(...), etc.) work on in-memory strings, independent of the file being open or closed at that moment.
'''