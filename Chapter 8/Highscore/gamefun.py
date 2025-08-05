#Game Function File
import random
def game():
    print("Welcome to random sum generator! This generates a sum of 2 numbers randomly generated from 1-10")
    y = random.randint(1,100)
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0      

    if y>highscore:  
            z = open("highscore.txt", "w")
            z.write(str(y))
            z.close()
            print("Score Added.")
            print(y)