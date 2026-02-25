# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    return s == s[::-1]  # Check if string is equal to its reverse

# Read input from user
text = input("Enter a string: ")

# Check and print result
if is_palindrome(text):
    print(f'"{text}" is a palindrome')
else:
    print(f'"{text}" is not a palindrome')

    #output
   #Enter a string: python 
   #"python" is not a palindrome