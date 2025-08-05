#Snake Water Gun Game! With lesser if else.
import random

'''
Rules.
Snake vs. Water: The snake drinks the water, so the snake wins. 
Water vs. Gun: The water drowns the gun, so the water wins. 
Gun vs. Snake: The gun shoots the snake, so the gun wins. 
Same Choice: If both players choose the same option, it's a draw. 
'''
l = {"Snake": 1, "Water": 2, "Gun": 3}
lrev = {1: "Snake", 2: "Water", 3: "Gun"}

random_key = random.choice(list(l.keys()))
random_value = l[random_key]
choices = "y"
while choices:
    random_key = random.choice(list(l.keys()))
    random_value = l[random_key]
    if choices.lower() == "y":
        print("Choose One of the three:")
        print("Press 1 for Snake: ")
        print("Press 2 for Water: ")
        print("Press 3 for Gun: ")
        ch = int(input("Choice? "))
        if random_value == ch:
            print(f"You chose {lrev[ch]}, computer chose {random_key}")
            print("Tie. You both chose the same option!")
            choices = input("Continue? Y/N: ")
        elif ch >= 4: #Moved this up.
            print("Wrong Choice!")
            choices = input("Retry? Y/N: ")
        else:
            if random_value - ch == 1 or random_value - ch == -2 or random_value - ch == 2:
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Win!")
                choices = input("Continue? Y/N: ")
            else: #Removed the entire condition as we can change it to a direct else.
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Lose!")
                choices = input("Continue? Y/N: ")
    else:
        break
#We used math to set certain conditions.

