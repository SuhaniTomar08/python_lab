# Read integer from standard input
num = int(input())

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(factorial)

#output
5
120