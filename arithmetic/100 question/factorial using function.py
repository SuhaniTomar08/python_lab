# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

result = factorial(num)

print(f"Factorial of {num} is {result}")

#output
#Enter a number: 14
#Factorial of 14 is 87178291200