#Constructors. Important.

class employee:
    status = "Verified"
    language = "Python"
    salary = 1900000

    def __init__(self, status, language, salary, name): #This is a DUNDER method in python. This specific needs no function call outside class to run, it runs for sure on its own!
        self.status = status
        self.language = language
        self.salary = salary
        self.name = name #Directly put the name variable here so you dont have to repeat line 31 and 27 everytime! Saves you time.
        print("I am creating an object.") 

    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    
    def greet(self):
        print(f"Hello, {self.status}")
    
    @staticmethod #--> Its a decorator. We will see what a decorator is in future!
    def greetstatic():
        print("Hey! No self variable is used here, so we use @staticmethod to remove the requirement of adding self here.")


harry = employee("Unverified", "JS", 0, "Harry") #As soon as you instantiate, the dunder method is called right here. Make sure all parameters are filled or it will error.
# harry.name = "Harry"
print(harry.salary, harry.language, harry.status, harry.name)

rohan = employee("Unverified", "C++", "10", "Rohan") #Same here. Now notice how you can tweak the dunder method to accept three parameters.
# rohan.name = "Rohan"
print(rohan.salary, rohan.language, rohan.status, rohan.name) #You will have to print all of the parameters to see the output.

#However, not all dunder methods are autocalled! Init is called in this case, yes.

#You can now on line 26 and 30 instantaneously give the data, if you want it changed. Saves you the rffort to change anything inside the class itself, since priority
#is given to the instance attributes.
