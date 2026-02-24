# Function to find maximum value in a tuple
def max_in_tuple(tpl):
    maximum = tpl[0] 
    for item in tpl:
        if item > maximum:
            maximum = item
    return maximum

input_tuple = tuple(map(int, input("Enter elements of the tuple separated by space: ").split()))

max_value = max_in_tuple(input_tuple)

print("Maximum value in the tuple is:", max_value)

#output
#Enter elements of the tuple separated by space: 4 7 2 9 5
#Maximum value in the tuple is: 9