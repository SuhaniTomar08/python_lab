# Function to check if tuple elements are unique
def are_elements_unique(tpl):
    seen = set()
    for item in tpl:
        if item in seen:
            return False
        seen.add(item)
    return True

input_tuple = tuple(map(int, input("Enter elements of the tuple separated by space: ").split()))


if are_elements_unique(input_tuple):
    print("All elements in the tuple are unique.")
else:
    print("The tuple contains duplicate elements.")

    #output
    #Enter elements of the tuple separated by space: 1 2 3 4 5
    #All elements in the tuple are unique.