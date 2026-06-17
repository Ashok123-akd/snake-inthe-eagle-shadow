'''
____________Day 4 (2083-03-03) wednesday by aashutosh dahal sir____________________________________________________

# two type of loop for and while loop
x=1
while x  <= 5:
    print (x)
    x  += 1

for i in range (6):
    print (i)


range(n)
range(start,stop)
range(start,stop,step)

Break and continue statement
for i in range (10):
    if i == 5:
        break
    print (i)

for i in range (10):
    if i == 5:
        continue
    print (i)

Nested loop---------------------------------------------------------------------------------------------------------
1. Grid &n Table 
outer = rows , inner = columns

2. patterns 
stars traingle, square, rectangle, diamond, pyramid, hollow triangle, hollow square, hollow rectangle, hollow diamond, hollow pyramid

3. multiplication table
classic nested loop example



'''

print ("_______________welcome to the game__________________")
name = input ("enter your name:")
age = int(input ("enter your age:"))
for i in range (age):
    print (name)

for i in range (10):
    if i == 5:
        break
    print (i)    

for i in range (10):
    if i == 5:
        continue
    print (i) #skips 5

for i in range (1,11):
    print ("*"*i) #prints a triangle pattern

for i in range (1,11):
    for j in range (1,i+1):
        print (j,end="\t") #prints table
    print() #for new line after each row of table







