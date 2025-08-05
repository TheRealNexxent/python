s1 = {7,8,1,78, 2}
s2 = {12,354,45,2}
s3 = s1.union(s2)
s4 = s1.intersection(s2)
s5 = s1-s2
print(s2.issubset(s1))
print({7, 8, 1, 78, 2, 20}.issuperset(s1))
print(s3)
print(s4)
print(s5)