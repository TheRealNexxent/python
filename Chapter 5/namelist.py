x = input("Enter name: ")
y = ["A", "B", "C", "D"]
if x.lower in y:
    print("Name exists in list.")
else:
    y.append(x)
    print("Name added, as was not in list")
    print(y)