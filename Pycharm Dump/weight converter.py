#Weight Conv

weight = float(input("Enter weight: "))
unit = input("Enter unit of measure (K OR L): ")

if unit == "K":
    weight = weight * 2.205
    print(f"Weight: is round.{weight}{unit}.")
elif unit == "L":
    weight = weight / 2.205
    print(f"Weight: is round.{weight}{unit}.")
else:
    print("Invalid unit!")


