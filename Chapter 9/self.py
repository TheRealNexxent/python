class employee:
    status = "Verified"
    language = "Python"
    salary = 1900000

    def getinfo(self): #This is a method. Or a function inside a class.
        print(f"The language is {self.language} and salary is {self.salary}")
    
    def greet(self):
        print(f"Hello, {self.status}")
    
    @staticmethod #--> Its a decorator. We will see what a decorator is in future!
    def greetstatic():
        print("Hey! No self variable is used here, so we use @staticmethod to remove the requirement of adding self here.")



harry = employee() 
harry.name = "Harry"
print(harry.salary,harry.language, harry.status, harry.name)

employee.salary = 100000 #---> This is like a pen write. You can put it anywhere. If you put here, then it wont affect harry's salary. Personalized.
rohan = employee()
rohan.name = "Rohan" 
print(rohan.language, rohan.salary, rohan.name) 

harry.getinfo() # Gives an error! Says 1 arg was given. Why? Cause, the command runs: employee.getinfo(harry) <--- Harry is the argument!
#So always put Self when defining the method/or function in class.

rohan.getinfo()

harry.greet()
harry.greetstatic()
#self is a convention, but you can write anything, vcc, rrrr, kasdjlask, etc. Just make sure to keep vcc.salary as well then and so on.
