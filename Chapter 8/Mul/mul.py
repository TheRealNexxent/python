for i in range(2,21):
    with open(f"{i}.txt", "w") as f:
        for j in range(1,11):
                    x = f"{i}*{j}={i*j}\n" #So it automatically gets set to string.
                    print(x)
                    f.write(x)

#Or alternatively
def gentable(n):
    table = ""
    for i in range(1,11):
        table += f"{n}*{i} = {n*i}\n"
    
    with open(f"tables/table{n}.txt", "w") as f:
        f.write(table)

for j in range(2,21):
     gentable(j)