'''
# Game Health system

i = int(input("enter health form 0-100 index:"))
if i > 70:
    print("player is healthy!")
elif i > 30  :
    print ("player is injured!")
elif i > 0 :
    print ("player is critical!")
else :
    print ("gameover!")
#Sleep and stress mood system

stress = int(input('enter stress level from 0-10:'))
sleep = int(input('enter Sleep level from 0-10:'))
if sleep < 5 and stress > 7 :
    print('exhausted')
elif sleep < 5:
    print('tired')
elif stress > 7:
    print('stressed')
else:
    print('normal')

# Movie ticket pricing

age = int(input("enter your age:"))
time = int(input('enter time from 0-12:'))
p = 10

if age < 12:
    print ('50% discount',p*50/100)
elif age >= 65 :
    print ("25% discount",p*25/100)
elif time < 5:
    print ("2$ discout for all",p-2)
else:
    print ('no changes')


'''


# Login system with multiple checks

u_name = input("enter username=")
p = input ("enter password=")
securitycode = int(input("enter your code="))

name="admin"
pa="secure123"
code=123

if u_name == name and p == pa :
    if  securitycode == code :
        print ("sucessfull login sucessfull")
else:
    print ("you have entered wrong detail!")






