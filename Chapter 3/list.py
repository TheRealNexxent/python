friends = ["Apple", "Orange", "Akash", 0, False, 2.3]
print(friends)
friends[0] = "Grapes"
print(friends)
#Mutable! UYnlike String, Lists are mutable. You can assign different values to list elements and change them. for strings you cant
#eg
'''y = "Hello"
y[0] = "h"  # This will raise an error because strings are immutable
print(y)'''

print(friends[3]) #Indexing same like as strings
print(friends[1:3]) #Slicing same like as strings
print(friends[-3:-1])


x = "apple"
print(x[-2:-1])  # Slicing a string

l = [1,2,3,4,5]
print(sum(l))
