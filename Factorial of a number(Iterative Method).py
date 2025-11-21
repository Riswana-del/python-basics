# Program to calculate factorial using iteration

# Get input from the user
num = int(input("Enter a number: "))

# Initialize factorial to 1
factorial = 1

# Factorial of negative numbers doesn't exist
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Multiply all numbers from 1 to num
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
