#Class with att a, and then create object from it and set 'a' directly using object.a = o. Does it change the class attribute?

class abc:
    a = "def"
o = abc() #Create an object from the class
print(o.a)#Prints class attribute cause instance attribute is not present until the next line.
o.a = "abc"
print(o.a)
#Now here it checks for instance attribute, finds the instance attribute and prints it. SO did the class attribute change?
#NO! Only the object/instance attribute has changed here!
#If you do:
print(abc.a)
#You will get the same value "def" again.
#It sets an instance attribute, but doesnt change the CLASS attribute!