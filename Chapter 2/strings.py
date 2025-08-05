x = input("Enter a string ")
x.find("  ")
x = x.replace("  ", "<doublespaces detected here!>").replace("a", "A") #you can put it twice too! Chaining, the first function becomes new string and then second works
print(x)
print("Letter = \"Dear Harry, this python course is nice. Thanks!\"")   
print(x.find("A"))