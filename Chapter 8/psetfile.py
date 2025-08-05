#Read from poems.txt and check if it has "twinkle"

x = open("poems.txt", "w")
x.write("Twinkle")
x.close()

# #or

with open("poems.txt", "w") as f:
    f.write("Twinkle")

z = open("poems.txt")
if "Twinkle" in z:
    print("Yes")
else:
    print("No")


