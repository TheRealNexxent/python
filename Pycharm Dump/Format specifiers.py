price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

#.xf for float accuracy
print(f"{price1:.2f}")
print(f"{price2:.2f}")
print(f"{price3:.2f}")

#space allocation
print(f"{price1:10}")
print(f"{price2:10}")
print(f"{price3:10}")
print(f"{price1:010}") #and if you put 010 then they will be zero padded.
print(f"{price1:<10}")
print(f"{price1:>10}")
print(f"{price1:^10}")
print(f"{price1:+}")
print(f"{price1: }")
print(f"{price1:,}") #Thousandth separator
print(f"{price1:+20,.2f}") #mixture