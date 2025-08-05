st = "Hey dude you are awesome!"

f = open("myfile.txt", "a")
f.write(st)
f.close()
#Now here, it unlike write, does not overwrite, but just adds the data you provide!
