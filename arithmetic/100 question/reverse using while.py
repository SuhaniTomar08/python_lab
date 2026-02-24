# Read integer from standard input
num = int(input())

sign = -1 if num < 0 else 1
num = abs(num)

rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

rev *= sign

print(rev)

#output
-1234

-4321