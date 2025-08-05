# translator = {
#     "Bhindi": "Ladies Finger",
#     "Brinjal": "Eggplant",
#     "Cabbage": "Cabbage",
#     "Carrot": "Carrot",
# }
# details = translator.keys()
# print("The vegetables in Hindi are: ", details)
# lookup = input("Enter a vegetable name in Hindi: ")
# print("The translation for this in english is: ", translator[lookup])

# numbers = set()
# n1 = input("Enter First number:")
# n2 = input("Enter Next number:")
# n4 = input("Enter Next number:")
# n5 = input("Enter Next number:")
# n3 = input("Enter Next number:")
# n6 = input("Enter Next number:")
# n7 = input("Enter Next number:")
# n8 = input("Enter Next number:")
# numbers.add(n1)
# numbers.add(n2)
# numbers.add(n3)
# numbers.add(n4)
# numbers.add(n5)
# numbers.add(n6)
# numbers.add(n7)
# numbers.add(n8)
# print("The numbers you entered are: ", numbers)

# setter = {1,2, "19"}
# print("The set is: ", setter)

# trial = set()
# trial.add(20)
# trial.add(20.0)
# trial.add('20')
# print(len(trial))
# print(trial) #Length is 2 because 20 and 20.0 are considered the same value in a set, and '20' is a different type (string). 1 == 1.0, try in REPL too!

# entry = {}
# key1 = input("Enter friend 1 name:")
# key2 = input("Enter friend 2 name:")
# key3 = input("Enter friend 3 name:")
# key4 = input("Enter friend 4 name:")
# val1 = input("Enter Lang 1 name:")
# val2 = input("Enter Lang 2 name:")
# val3 = input("Enter Lang 3 name:")
# val4 = input("Enter Lang 4 name:")

# entry.update({key1: val1})
# entry.update({key2: val2})
# entry.update({key3: val3})
# entry.update({key4: val4})

# print("The dictionary is: ", entry)
# # Even in dictionaries, keys must be unique. If you try to add a duplicate key, it will overwrite the previous value associated with that key. Basically UPDATES.
# # But values can be duplicated. For example, if two friends speak the same language, you can have the same value for different keys.

# s = {1,2,3, "a", [1,2]}
# print(s) #List cannot be added to set.
#print(hash(list())) returns error because lists are mutable and cannot be hashed.
