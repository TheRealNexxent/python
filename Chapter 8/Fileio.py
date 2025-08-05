#Volatile: Data does not persist on it. Ex: Data intermediatery, the variable data for example, or a functions return value, will not persist in the RAM. Volatile!
'''
a = "asdasdhasjkldhaslkjdalskdas

emails = []
Suppose 3 sec to complete the program.
Accoring to the code given, The Emails generate here, and then its over. Nothing else happens!
It does not persist.

To solve this, we need to have a FILE that saves all this before it doesnt persist. Like a text file, a notepad file, mp3 file, etc.
All thes files have data stored. All the generated code output, if you want it to persist in the disk, then you need to use the FILE I/O.
Persist == Save, or exist on the Hard Drive. You want it to save on ROM, or HDD, not RAM!

Then why dont we use HDD itself from the start? Because RAM is FAST! HDD is slow. Useful for fast code execution.

2 Types of files: Text files[.py,txt], and Binary Files. Binary files ex: .jpg, .bat
'''
import os
print(os.getcwd())

f = open("file.txt") #You can also put different read modes, ,like: ("filename", "r/w"). Also, R is by Default.
data = f.read()
print(data)
f.close() #Always close the file too! Else it wastes memory.