name = input("Enter your name: ")
result = len(name)
res = name.find("n") #0,1,2,3,4,5
res1 = name.rfind("s")
print(result)
print(res)
print(res1) #Will return -1 if not findable
name = name.capitalize()
print(name)
res2 = name.upper()
print(res2)
res3 = name.lower()
print(res3)
res4 = name.isdigit() #Will return true only if all chars are digits
print(res4)
res5 = name.isalpha()
print(res5) #All chars

phone = input("Enter your phone number: ")
res6 = phone.count("9")
print(res6)
res7 = phone.replace("9", " ")
print(res7)
# Use this for more str methods. print(help(str))
