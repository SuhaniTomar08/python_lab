# Function to count frequency of elements
def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

frequency = count_frequency(input_list)

print("Frequency of elements:")
for key, value in frequency.items():
    print(f"{key}: {value}")

    #output
    #Enter elements of the list separated by space: 7
    #Frequency of elements:
    #7: 1