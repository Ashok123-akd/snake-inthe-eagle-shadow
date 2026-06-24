'''
lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.
'''

triple = lambda x: x*x
print (triple(5)) #prints 25
print (triple(10)) #prints 100
print (triple(15)) #prints 225


def greet():
  print("greet")
  greet()

greet()