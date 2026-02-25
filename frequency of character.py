<<<<<<< HEAD
# Program to find frequency of each character

text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

for key in freq:
    print(key, "->", freq[key])
"""Output

Enter a string: apple
a -> 1
p -> 2
l -> 1
=======
# Program to find frequency of each character

text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

for key in freq:
    print(key, "->", freq[key])
"""Output

Enter a string: apple
a -> 1
p -> 2
l -> 1
>>>>>>> 422e0177c51f10c37b5ebf1614fa14d3714e9bd1
e -> 1"""