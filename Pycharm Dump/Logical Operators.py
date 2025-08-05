temp = 30
is_raining = False
if temp > 35 or is_raining or temp < 0:
    print("Event cancelled!")
else:
    print("Event happening!")

temp1 = 2
is_sunny = False
if temp1 >= 28 and is_sunny:
    print("Gday to drive.")
elif temp1 <= 0 and is_sunny:
    print("Car is super chilled, but might be able to heat it up in this sunny weather.")
elif temp1 >= 0 and not is_sunny:
    print("DONT GO OUT")
else:
    print("Engine probably super chilled.")

num = 5 #Conditional Expression
a = 6
b = 5
print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)
max_num = a if a>b else b
min_num = a if a<b else b
print(max_num, min_num) 