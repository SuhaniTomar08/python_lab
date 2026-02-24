# Read username and password from standard input
username = input()
password = input()

if len(username) >= 5 and len(password) >= 8:
    print("Valid")
else:
    print("Invalid")

    #output
    #user123
    #mypassword

    #Valid

    #usr
    #pass

    #Invalid
