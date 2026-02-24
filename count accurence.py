# Function to count occurrences of an element in a tuple
def count_occurrences(tpl, element):
    count = 0
    for item in tpl:
        if item == element:
            count += 1
    return count

input_tuple = tuple(map(int, input("Enter elements of the tuple separated by space: ").split()))

element = int(input("Enter the element to count: "))

occurrence = count_occurrences(input_tuple, element)

print(f"The element {element} occurs {occurrence} time(s) in the tuple.")


#output
#Enter elements of the tuple separated by space: 1 2 3 2 4 2 5
#Enter the element to count: 2
#The element 2 occurs 3 time(s) in the tuple.