# Read input string
text = input("Enter a string: ")

count = 0

vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#output
#Enter a string: armstrong
#Number of vowels: 2