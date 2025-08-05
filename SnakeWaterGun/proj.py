#Snake Water Gun Game!
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
        else:    
            if random_value == 2 and ch == 3:
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Lose!")
                choices = input("Continue? Y/N: ")
            elif random_value == 2 and ch == 1:
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Win!")
            elif random_value == 1 and ch == 2:
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Lose!")
                choices = input("Continue? Y/N: ")
            elif random_value == 1 and ch == 3:
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Win!")
                choices = input("Continue? Y/N: ")
            elif random_value == 3 and ch == 1:
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Win!")
                choices = input("Continue? Y/N: ")
            elif random_value == 3 and ch == 2:
                print(f"You chose {lrev[ch]}, computer chose {random_key}")
                print("You Lose!")
                choices = input("Continue? Y/N: ")
            else:
                print("Wrong choice!")
                choices = input("Retry? Y/N: ")
    else:
        break
