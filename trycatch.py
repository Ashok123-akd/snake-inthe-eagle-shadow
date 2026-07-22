# Exception handling 2083-03-31(wednesday)__________________________________________________________________________
try:
    num = int(input("enter number :"))
    print(100/num)
except :
    print ("your input is invalid")

'''
try :
    # Risky code 
catch:
    # Recovery code

try:
    num = int(input())
    print(100/num)
except ValueError:
    print("numbers only.")
except ZeroDivisionError:
    print("cannot divide by zero.")

SEPERATE EXCEPT BLOCKS

except valueError:
    print("numbers only.")
except ZeroDivisionError:
    print("cannot divide by zero.")

TUPLE IN ONE EXCEPT

except (ValueError, ZeroDivisionError):
    print("numbers only or cannot divide by zero.")

    
CATCH ALL WITH AS E

except Exception as e:
    print("Error is : ", e)

    
__________________________________ THE FINALLY BLOCK _______________________________________

try:
    file = open("test.txt", "r")
except FileNotFoundError:
    print("file not found")
finally:
    print("this block will always execute")

    

    
    
'''

try:
    num = int(input())
    print(100/num)
except ValueError:
    print("numbers only.")
except ZeroDivisionError:
    print("cannot divide by zero.")

'''
UNIVERSITY ELIGIBILITY CHECKER___________________________________________________________________________________

try:
    file = open("test.txt", "w")
except FileNotFoundError:
    print("file not found")
finally:
    print("this block will always execute")

try:
    age = int(input("Enter your age: "))
    percentage = float(input("Enter your +2 percentage: "))

    if age < 17:
        print("Not Eligible: Minimum age should be 17 years.")
    elif percentage < 50:
        print("Not Eligible: Minimum percentage should be 50%.")
    else:
        print("Congratulations! You are eligible for university admission.")

except ValueError:
    print("Error: Please enter valid numeric values.")

finally:
    print("Eligibility check completed.")
'''
