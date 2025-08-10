#Methods

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


p1 = person("Ben")
p2 = person("Jim")
print(person.number_of_people_())