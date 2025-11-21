# Program to print all prime numbers up to a given number

# Get input from the user
n = int(input("Print prime numbers up to: "))

print("Prime numbers up to", n, "are:")

# Loop through numbers from 2 to n
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # Check up to square root
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
