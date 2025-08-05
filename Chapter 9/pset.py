#Programmers Class
class programmer:
    empid = int
    name = str
    designation = str
    age = int
    ctc = float

    def __init__(self):
        print("Welcome to the Programmerdata for Microsoft! Here is all the data requested for the employee:")
        # self.empid = empid
        # self.name = name
        # self.designation = designation
        # self.age = age
        # self.ctc = ctc ----> Use all this as alternative if you want to run code in line 27 methodology.
    
    def newemp(self):
        self.empid = int(input("Enter EmpID: "))
        self.name = input("Enter Name: ")
        self.designation = input("Designation? ")
        self.age = input("Age? ")
        self.ctc = input("CTC? ")
        print(f"The Data finalized is:\n{self.empid}\n{self.name}\n{self.designation}\n{self.age}\n{self.ctc}")


# divyansh = programmer(1, "Divyansh", "SDE1", 22, 1200000)
# print(divyansh.empid, divyansh.name, divyansh.designation, divyansh.age, divyansh.ctc)

divyansh = programmer()
divyansh.newemp()
print(divyansh.empid)