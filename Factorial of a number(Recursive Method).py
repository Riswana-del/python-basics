# Program to calculate factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
