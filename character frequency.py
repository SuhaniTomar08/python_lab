# Program to count character frequency using dictionary

text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print("Character frequency:")
for key in freq:
    print(key, "->", freq[key])

    #output
    #Enter a string: apple
#Character frequency:
#a -> 1
#p -> 2
#l -> 1
#e -> 1