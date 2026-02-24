# Function to find second largest element
def second_largest(lst):
    if len(lst) < 2:
        return None 
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float('-inf'):
        return None 
    return second


input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

result = second_largest(input_list)

if result is None:
    print("No second largest element found.")
else:
    print("The second largest element in the list is:", result)

    #output
    #Enter elements of the list separated by space: 8
    #No second largest element found.