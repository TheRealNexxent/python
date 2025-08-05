#[] operator, [start:end:step], where start index starts from 0, is inclusive, and ending index is EXCLUSIVE.

credit = "1234-5678-9012-3456"
print(credit[0])
print(credit[0:4]) #or print(credit[:4])
print(credit[5:9])
print(credit[15:])
print(credit[-1]) #or backwards!
print(credit[::2])

last_digits = credit[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
credit2 = credit[::-1]
print(credit2) #Reverse the string, step to -1.
