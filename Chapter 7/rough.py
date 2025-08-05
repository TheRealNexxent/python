
l = ["aaaaaan","baaan","can"]

def rem2(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
print(rem2(l,"an"))