#Chapter 1: Get introduced to typing snek code!

import math
import os
import pyttsx3 #Modules.
print('''Oh look a new program! Without Hello world!
      asdsadasdsa
      asdasdsa
      dassadas
      dsadasd
      asdsd''') #To Print something.
r = math.sqrt(4) #Through the math module.
print(r)
help(os)
os.listdir() #To list the directory elements. Or the folder you are in, basically.
engine = pyttsx3.init()
engine.say("Hello world. Nevermind. I said it twice.")
engine.runAndWait()