def addition():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The result of addition is:", num1 + num2)


def subtraction():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The result of subtraction is:", num1 - num2)


def multiplication():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The result of multiplication is:", num1 * num2)


def division():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        print("The result of division is:", num1 / num2)
    else:
        print("Error: Division by zero")


def main():
    print('Welcome')
    while True:
        print("Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Which operation do you want from the menu above? (1-5) ")

        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            multiplication()
        elif choice == '4':
            division()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()

