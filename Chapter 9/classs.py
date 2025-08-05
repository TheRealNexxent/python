#Solving a program by creating objects, is called OOP.
#DRY Method: Dont repeat yourself methodology.
#One of the most popular approaches!
#The other approach is Funtional Programming.
#Classes and objects!
#Class is a blueprint to create an object.
#Like an Exam form. You fill it, it becomes personzalized. But until its not filled, its a Blueprint. A Class! Not an object!
#When the class is empty, its like a placeholder.


#NOTE: Example Class!
class employee:
    status = "Verified"
    language = "Python"
    salary = 1900000

employee.salary = 100000 #Changing Class Attribute.

harry = employee() #Object/Instance instantiation.
harry.name = "Harry"
print(harry.salary,harry.language, harry.status, harry.name)

rohan = employee()
rohan.name = "Rohan" #Here, name is Object/Instance attribute! It doesnt directly belong to the class.
print(rohan.language, rohan.salary, rohan.name) #Salary and Language are class attributes, since they are directly linked to the class.


#Object is an instantiation of a class! As long as object is not instantiated, the memory will not be allocated to the object.
#Generally:
#Noun: Class: Empoloyee
#Adjective: Object: Age, Salary, Married
#Verbn: Methods: getage(), getsalary(), getmaritalstatus()

#Class attributes belong to class directly, not the object.
