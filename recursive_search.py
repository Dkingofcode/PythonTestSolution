
#  Write a recursive searching algorithm to search for a number in a list of numbers
def RecursiveSearch(target, numbers, i=0):
    # Base case: If the index is equal to the length of the list, the element is not found.
    if i == len(numbers):
        return False

    # Check if the current element is equal to the target.
    if numbers[i] == target:
        return True
    else:
        # Recursive case: Increment the index and call the function again.
        return RecursiveSearch(target, numbers, i + 1)
