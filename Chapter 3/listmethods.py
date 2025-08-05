friends = ["Apple", "Orange", "Akash", 0, False, 2.3]
print(friends)

friends.append("Grapes")  # Adding an element to the end of the list
print(friends)
#Mutability, will change the list itself, not create a new list.

x = ["1", "2", "3", "7", "9", "8"]
x.sort()
print(x)
x.reverse()
print(x)
x.reverse()  # Reversing the list
print(x)

x.insert(2, "0")
print(x)  # Inserting "0" at index 2
x.pop(2)
print(x)  # Removing the element at index 2
print(x.pop(0))
print(x)
x.remove("8")
print(x)


y = ("1", "Abby", 2, True)
print(type(y))
print(y)

z = (1, 1, 1, 2, 1) #Tuple with 1 element requires a comma in the end, or it wont be recognized as tuple type
#Tuple elements cannot be changed, they are immutable
print(z.count(1))  # Count the number of occurrences of 1 in the tuple
print(z.index(2))
print(len(z))  # Length of the tuple

q = (1,2,3)
r,s,t = q
print(r, s, t)  # Unpacking the tuple into variables

fruit = list(input("Enter the Fruit names, each separated by a comma!").split(","))
print(f"The Fruits are: \n {fruit}")

marks = list(map(int, input("Enter the marks of the students, each separated by a space!").split()))
marks.sort() #Dont do marks = marks.sort(), that just retyrns none cuz sorting was successful and it returned 0 or none. instead use normalk and print
print(marks)


x = ["1"]
map(int, x)
print(type(x))  # This will still print <class 'list'> because map returns a map object, not a list
print(x)