class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade

class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("True")
        else:
            print("False")
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)


s1 = student("Tim", 19, 95)
s2 = student("Jim", 19, 75)
s3 = student("Nim", 19, 65)

course = course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3) #Wont work, since mnax student is 2!
print(course.get_average_grade())