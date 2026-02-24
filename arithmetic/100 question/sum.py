# Read integer from standard input
num = int(input())

sum_digits = 0

num = abs(num)

while num > 0:
    sum_digits += num % 10
    num = num // 10

print(sum_digits)

#output
1234
10