while True:
    try:
        # Ask for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Try to divide
        result = num1 / num2
        print("Result of division is:", result)

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue  # Go back to the start of the loop
    
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a different second number.")
        continue

    # Ask if the user wants to continue
    choice = input("Do you want to divide another set of numbers? (yes/no): ").strip().lower()
    if choice != "yes":
        print("Goodbye!")
        break
