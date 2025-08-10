#Superclass

class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    def speak(self):
        print("I dont know what animal I am!")


class cat(pet): #Inherited parent class in braces. 
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Mew!")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, and {self.color} in color")


c = cat("Pinkie", 12, "Blue")
c.show()

#Here, we called a superclass attribute name age, so it initialized the line 5 6 variables for us, and then we developed on it to add a color as well. no need to recopy the whole method, as that could lead to errors in database management scenarios. If it had database information, and if you needed something specific, it would be better to call those specific ones.

#Like, if you had a parent class called Person, and then 2 child classes called Manager and Employee, then the parent class would have all data on the person class, employee or manager irrelevant, and then you can selectively add the attributes, NOT ALL ATTRIBUTES, to each child class.

