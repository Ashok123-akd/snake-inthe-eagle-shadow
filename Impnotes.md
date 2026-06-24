# snake-inthe-eagle-shadow

Flexing Python from the skies. -------Flying Python-------------------------------
This is the best class of my life. I don't have any idea what I doing , trying to hustle flex and learn some coding basics with the tutor and the boys!
keep calm and learn python..
Welcome to my cave.....
open the wave, lets bring the vibe open the vs code...

**\*\***\_\_\_**\*\***what is variable????
Variable is a container to store information. It is a named storage location that holds value in a program.
correct variable naming:
stu_dent
age
\_stu_dent
stuDent

Naming is very case senstive, please keep this in mind.

Cases:
snake case

Data types:
Integer- (int) ex:20,120,21,
Float- (float) ex: 36.3,333.666,-2.5
String- (str) should be inside this:""
Boolean- (bool)

The Input() Function
why type conversion:
becasue input returns everything as string, to perform math ops,

is_foody = input("are you foody?(yes/no):").trim().lower() this is the best practice

ARthimetica and Assignment operator:
Operator : + - _ %=returns remainder /=divide one number by another
Assignent operator:
= -> assign a value
== -> checks equal
+=
-=
_=
/=
===========================================================================================================================

-------------2083/02/29 (Friday)----------------------

The if Statement
if condition:
statement

then if-else statement
if condition:
else:
ex:
marks=50
if marks >=40:
print("pass")
else:
print("fail")

-

Nested IF= It is typically used to check multiple cases one after another---------------------------------------------------
age=20
marks = 80
if age >= 18:
if marks >= 60:
print("Eligible")

elif (Ladder)----------------------------------------------------------------------------------------------------------------

markss =85
if marks >= 80:
print("A grade")
elif marks >= 60:
print("B grade")
elif marks >= 40:
print("C grade")
else:
print("fail")

Logical Operator------------------------------------------------------------------------------------------------------------
Nested loop---------------------------------------------------------------------------------------------------------

1. Grid &n Table
   outer = rows , inner = columns

2. patterns
   stars traingle, square, rectangle, diamond, pyramid, hollow triangle, hollow square, hollow rectangle, hollow diamond, hollow pyramid

3. multiplication table
   classic nested loop example

---------------------FUNCTION IN PYTHON (2083-03-10 -wednesday)-----------------------------------------------
Unknown number of input

\_\_VARIABLE LENGTH ARGUMENT
def add(a,b):
return a+b
add(5,10) --works for this
add(5,6,7,8) -- doesn't work for this

def function_name (\*args):

what is *args?
*args allows a function to receive any number of positional arguments

def function_name(\*args):

def add_numbers(\*numbers):
total = sum(numbers)
return total

print(add_number(1,2)) (1,2)--these are stored as tuples in python a form of data structure
print(add_number(1,2,3,4,5))

NOW! let's talk about *kwargs******\*\*******\*\*******\*\*******\_\_******\*\*******\*\*******\*\*******KWARGS!KWARGS!KWARGS!KWARGS\_**\_kwargs!**kWARGS!
*keywordargument---
\*kwargs allows the function to recieve any number of named arguments

SYNTAX:
def student_info (\**kwargs)
print(*kwargs)

student_info(name="Ashok",age=26,city="kathmandu")

{'name':'Ashok', 'age':26, 'city':'kathmandu'}

python stores arguments as dictionary

we use kwargs ["variable_name"] to access the individual elements

def student_info(\*\*kwargs):
print("Name",Kwargs["name"])
print("Age:",Kwargs["age"])
student_info(name="Ram",age=18)

********\_\_\_\_********LAMBDA FUNCTION******************\_\_\_******************

It is used to create short operation without creating full function.
It is refrered to as one line function
they are commonly used with sort(),map() and filter() function.


_________Recursion _____________________
What is recursion?
Recursion occurs when a function calls itself.
every refcursive functions needs
_Base case 
Stopping condition
_Recursive Case
Fucntion calls itself 

without a base case recursion never ends.

def greet():
  print("greet")
  greet()

greet()


def factorial(n):
  if n == 1:
    return 1
  return n * factorial (n - 1)
print (factorial(5))
#here each time the number is  being decreased and the factorail is being called to find the factorial.

def fibonacci (n):
  if n <= 1:
    return n
  return fibonacci (n-1) + fibonacci(n-2)

print (fibonacci(6))





