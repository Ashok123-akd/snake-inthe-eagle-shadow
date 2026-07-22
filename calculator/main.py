# main.py

import operations
from menu import display_menu

while True:
    display_menu()

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Thank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice!")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result =", operations.add(num1, num2))

    elif choice == "2":
        print("Result =", operations.subtract(num1, num2))

    elif choice == "3":
        print("Result =", operations.multiply(num1, num2))

    elif choice == "4":
        print("Result =", operations.divide(num1, num2))

    elif choice == "5":
        print("Result =", operations.modulus(num1, num2))

    elif choice == "6":
        print("Result =", operations.power(num1, num2))