# Read a single character from standard input
ch = input().lower()

if ch.isalpha():
    if ch in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Input")

    #output
    #E
    #Vowel