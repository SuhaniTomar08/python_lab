# Function to calculate sum of digits
def sum_of_digits(n):
    total = 0
    n = abs(n) 
    while n > 0:
        total += n % 10 
        n //= 10         
    return total

num = int(input("Enter a number: "))

result = sum_of_digits(num)

print(f"Sum of digits of {num} is {result}")

#output
#Enter a number: 12
#Sum of digits of 12 is 3