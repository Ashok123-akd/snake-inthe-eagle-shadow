'''
_____________________________Module Package_____________________________
modules is a .py file containing variable and functions which can be used in other .py file.
To use a module in another file we can use import statement.
IMPORTING MODULES
                import math
                from math import sqrt
                from math import sqrt, factorial
                import math as m
                from math import *

_______________________PACKAGE____________________________
project
    main.py
    utilities/
        _init_.py
        math_utils.py
        string_utils.py         

        
The datetime Module_____________

import datetime
today = datetime.date.today()
now = datetime.datetime.now()

print(today)
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 2024-01-15 14:30:45
print(now.strftime("%A, %B %d, %Y")) # Monday, January 15, 2024
print(now.strftime("%I:%M %p")) # 02:30 PM

%B/%A = Monthname/Dayname
%H:/%M:%S = Hour/Minute/Second
%I:%M %p = Hour:Minute AM/PM



THE OS MODULE_____________________________________________________________________________________

import os 
os.getcwd()
os.listdir(".")
os.mkdir("data")
os.rename("old.text", "new.txt")

'''
import math
math.sqrt(25)
math.pow(2,8)
math.factorial(5)
math.ceil(4.2)
math.floor(4.8)
math.pi
math.e


import random
random.randint(1,100)
random.random()
random.choice(["apple", "banana", "cherry"])
random.uniform(1.5, 10.5)

my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
random.shuffle(my_list)
