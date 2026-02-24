# Read number, lower bound, and upper bound from standard input
num, lower, upper = map(float, input().split())

if lower <= num <= upper:
    print("Within Range")
else:
    print("Out of Range")

    #output
    #15 10 20
    #Within Range

    #25 10 20
    #Out of Range