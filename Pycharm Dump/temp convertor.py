#Temp Conv

unit = input("Enter unit (C/F): ")
temp = float(input("Enter temperature: "))
if unit == "C":
    F = temp * (9/5) + 32
    print(f"Fahrenheit: {F}.")
elif unit == "F":
    C = (temp - 32) * 5/9
    print(f"Celsius: {C}.")
else:
    print("Invalid unit!")