#Static Methods

def add1():
    pass
def add2():
    pass
def add3():
    pass

#To group them all into one class, you can use a static method:

class math:
    @staticmethod #Not changing, staying the same.. do not have access to any instance. They dont change anything.
    def add5(z): #Needs no parameters, since its a function with no requirement.
        return z + 5
    
    @staticmethod
    def pr():
        print("Run")
        
print(math.add5(6)) #Needs no n = math() or any bs. Straight up link the class with the staticmethod.
math.pr()
