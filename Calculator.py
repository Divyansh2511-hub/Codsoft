print("Welcome to the Calculator ")
    
num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
    
choice = input("Choose Between (1-4): ")
    
if choice == '1':
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is: {result}")
elif choice == '2':
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is: {result}")
elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is: {result}")
elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is: {result}")
        else:
            print("Error! Division by zero is not possible.")
else:
        print("Invalid input!")