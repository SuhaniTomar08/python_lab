# Read three integers from standard input
a, b, c = map(int, input().split())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

    #output
    #10 25 15
    #25