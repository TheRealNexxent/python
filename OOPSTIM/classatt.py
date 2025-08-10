#Class Attributes are defined outside instances of the class or methods, they do not change on basis of self etc. They are defined for the entire class! They dont change based on self.

class person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        person.number_of_people += 1

p1 = person("Ben")
print(person.number_of_people) #Here it returns 1
p2 = person("Jim")

print(p1.number_of_people) #Then here it returns 2
print(p2.number_of_people)
print(person.number_of_people)

#All three will give same output since its not dependent on any object or instance of class. 

person.number_of_people = 10
print(person.number_of_people)
print(p1.number_of_people)
print(p2.number_of_people)

#Here it changed only based on the class data. It also auto changed all people's data to 10
 
p1.number_of_people = 11
print(p1.number_of_people)
print(p2.number_of_people)
print(person.number_of_people)

#Here only p1 data changed, not for others. Explicit change.

#Classes are exportable too. Thats why they are so useful for having properties migrated to other files. So the idea is to make the classes as detailed as possible.

