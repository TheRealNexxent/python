# OOPS IN PYTHON

`x = 1`  
>Here, 1 is the object of class int.  

`print(type("Hello))`  
>Here, Hello is object of class str.  
Basically they are all part of classes as objects.

Objects are everywhere in python.

```py
def hello():
    print("Hello!")

print(type(hello))
```

>Here this is also object of class function!

`print(x+hello)`  
>This will do nothing since both are objects of different classes and not of same types either.

```py
strings = "hi"
print(strings.upper())
```

>Here upper is a method of class str and strings is an object.

We will eventually also move on from these **BUILT IN** classes to our own made classes.

```py
class dog:
    def bark(self):
        print("Woof!")
```

>Here we have created a class dog, and added a method, which is basically a function within a class.

`d = dog()`

>Here, I've assigned an instance of the class dog to variable a!  
If I print the type of d, it will give __main__ since by default its module main.

## The Init Method

Now, there is a special method always called as soon as you run an instance of the class, for example:


`d = dog()`

```py
def __init__(self):
    pass
```

Is the basic syntax.  
>The benefit is you do not have to call this method explicitly!  
Self attributes like `self.name` can be referenced later as well outside the class, or in different methods inside the class.

## Why use Classes?

Well, let's take an example.  
`dog1 = "avbe"`  
`dog2 = "asdas`  
Adding all these dog names manually is a lengthy process, specially if you have 25000 dogs!

If we use lists:  
`dognames = [a,b,c]`  
`dogages = [1,2,3]`  
Again wont be good, since index searching for multiple values is a computer time consuming task!

Hence, classes and objects are always the better choice for large scale programs.


## Masterclass

```py
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
```

Here, we created a specific class student, and want to link it to another class course:

```py
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
```

Now, here since we have given max student count as 2, then adding s3 student would not give any output.

`course.add_student(s3)` will return error.

## Inheritance

> The show method is **INHERITED** once you type in the parent class in braces!

>Now, if there is a similar method in child class defined, here in this case `speak`, then it will auto override the child method to be used. If you dont specify, then it will take the `speak` method from above! 

It's also cool to know you have to still make a class for a different pet youre workin on  right now, ex: fish class.

## Superclass

```py
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

```

>Here, we called a superclass attribute name `age`, so it initialized the `line 5 6 ` variables for us, and then we developed on it to add a `color` as well. 

No need to recopy the whole method, as that could lead to errors in database management scenarios. If it had database information, and if you needed something specific, it would be better to call those specific ones.  

>Like, if you had a parent class called Person, and then 2 child classes called Manager and Employee, then the parent class would have all data on the person class, employee or manager irrelevant, and then you can selectively add the attributes, NOT ALL ATTRIBUTES, to each child class.

`super().__init__(name, age)` Is the syntax to selectively call attributes from parent class.


## Class Attributes.

```py
class person:
    number_of_people = 0
    def __init__(self, name):
        self.name = name
        person.number_of_people += 1
```

Here, `number_of_people` is the attribute defined inside the class.

>Class attributes are independent of object or instance of class. You can modify each instance's attribute individually, but in general if you do something like  
`person.number_of_people = 1`  
It will change the values for each variable p1 p2 p3 etc.

>Classes are `exportable` too. Thats why they are so useful for having properties migrated to other files. So the idea is to make the classes as detailed as possible.

## Class Methods

```py
class person:
    number_of_people = 0
    gravity = -9.8
    def __init__(self, name):
        self.name = name
        # person.number_of_people += 1 need not be typed anymore. Instead:
        person.add_people()
    @classmethod
    def number_of_people_(cls): #Cls methods have no access to self, and are intended to be used for the Class itself.
        return cls.number_of_people
    
    @classmethod
    def add_people(cls):
        cls.number_of_people += 1
```

Classmethods are explicitly defined as decorators through `@classmethod`

>The benefit is `number_of_people += 1` need not be typed anymore. Instead: `person.add_people()` gets the job done.

Cls methods are inaccessible through self, and are specifically used for classes itself.

## Static Methods
>To group them all functions into one class, you can use a static method:

```py
class math:
    @staticmethod #Not changing, staying the same.. do not have access to any instance. They dont change anything.
    def add5(z): #Needs no parameters, since its a function with no requirement.
        return z + 5
    
    @staticmethod
    def pr():
        print("Run")
```

> Static methods are `Not changing, staying the same..` do not have access to any instance. `They dont change anything.`

