#Inheritance!

class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    def speak(self):
        print("I dont know what animal I am!")


class cat(pet): #Inherited parent class in braces. 
    def speak(self):
        print("Mew!")

class dog(pet):
    def speak(self):
        print("Woof!")

class fish(pet):
    pass


p = pet("Weewoosh", 12)
p.show()
p.speak()

c = cat("Pinkie", 12)
c.show()
c.speak()

d = dog("Bleh", 11)
d.show()
d.speak()

f = fish("Bleh", 12)
f.show()
f.speak()


#The show method is INHERITED once you type in the parent class in braces!
#Now, if there is a similar method in child class defined, here in this case speak, then it will auto override the child method to be used. If you dont specify, then it will take the speak method from above! It's also cool to know you have to still make a class for a different pet youre workin on  right now, ex: fish class.

