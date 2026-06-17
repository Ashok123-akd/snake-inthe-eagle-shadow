'''
age= int(input("enter  age:"))
height= float(input("enter  height:"))
name = input("enter your name:")
is_foody = input("are you foody?(yes/no):")


#is_foody = input("are you foody?(yes/no):").trim().lower() this is the best practice



print('You are',age,'old.')
print('this is your height',height)
print('this is your name',name)

if is_foody.lower()== "yes":
    print("you are foody. That is awesome. Invite me someday please.Let's have dinner together.")
else:
    print('you are not foody you are vegetable. you are the best.........')




 Wrong ______________________________________________________________
foody = bool(input("enter yes or no:"))
if foody.yes == True :
    print ("your are foody")
'''

'''_____________________Only prints last value______________________________
i=2
i += 10 
i -= 10
i *= 10
i /= 10
print(i)
'''
'''
i=2
i += 10 
print(i)
i -= 10
print(i)
i *= 10
print(i)
i /= 10
print(i)

'''

age = 20
is_citizen = True
can_vote = (age >= 18 ) and (is_citizen)
print(can_vote) #output true

marks = 75
attendance = 85

passed = (marks >=40) and (attendance >= 75)
print (passed) #output true




