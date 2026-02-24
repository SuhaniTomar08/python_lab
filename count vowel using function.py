# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")

num_vowels = count_vowels(text)

print(f"The number of vowels in '{text}' is {num_vowels}")

#output
#Enter a string: start
#The number of vowels in 'start' is 1