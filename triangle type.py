# Read the three sides of a triangle from standard input
a, b, c = map(float, input().split())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Triangle")

    #output
    #5 5 5
    #Equilateral Triangle

    #5 5 8
    #Isosceles Triangle