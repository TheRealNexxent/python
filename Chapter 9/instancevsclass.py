class employee:
    status = "Verified"
    language = "Python"
    salary = 1900000

employee.salary = 100000 

harry = employee() 
harry.name = "Harry"
print(harry.salary,harry.language, harry.status, harry.name)

rohan = employee()
rohan.name = "Rohan" 
rohan.salary = 1000 #Here, Instance will always be given priority over class attribute if you make a change. Instance takes preference over class.
#HOWEVER THAT DOESNT MEAN THE CLASS ATTRIBUTE GOT CHANGED, NO! ONLY THE INSTANCE ATTRIBUTE IS GETTING PRINTED ON PRIORITY! ITS NOT CHANGING ANY
#CLASS ATTRIBUTE! REFER TO CLAATT.PY FOR A QUESTION ON THIS FOR CLARITY.
print(rohan.language, rohan.salary, rohan.name) 


# Basically, priority check follows as such:
# 1. Is Attribute present in Object? If yes then proceed with this step
# 2. Else, go with class attribute.

