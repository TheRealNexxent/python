#Validate the following policies in a password
#Not more than 12 chars
#No spaces
#No digits
choice = "Y"
while choice:
    if choice == "Y":
        str1 = input("Enter your password: ")
        if not str1.isalpha() and str1.isnumeric():
            print("Your password contains digits.")
            choice = input("Would you like to retry? [Y/N]")
        elif not str1.find(" ") == -1:
            print("Your password contains spaces.")
            choice = input("Would you like to retry? [Y/N]")
        elif len(str1) > 12:
            print("Your password is too long.")
            choice = input("Would you like to retry? [Y/N]")
        else:
            print("Password Accepted.")
            break
    else:
        break


