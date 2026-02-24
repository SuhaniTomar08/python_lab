# Function to find minimum value in a tuple
def min_in_tuple(tpl):
    minimum = tpl[0]  
    for item in tpl:
        if item < minimum:
            minimum = item
    return minimum

input_tuple = tuple(map(int, input("Enter elements of the tuple separated by space: ").split()))

min_value = min_in_tuple(input_tuple)

print("Minimum value in the tuple is:", min_value)

#output
#Enter elements of the tuple separated by space: 4 7 2 9 5
#Minimum value in the tuple is: 2