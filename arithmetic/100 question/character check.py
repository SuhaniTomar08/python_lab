# Read a single character from standard input
ch = input()

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Invalid Input")

    #output
    #7
    #Digit