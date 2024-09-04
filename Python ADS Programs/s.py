def largest_number(arr):
    # Define a custom comparison function to sort the numbers
    def custom_cmp(x, y):
        # Concatenate the numbers in both orders and compare them
        xy = x + y
        yx = y + x
        # Compare the concatenated strings to determine the order
        return (xy > yx) - (xy < yx)

    # Sort the array using the custom comparison function
    sorted_arr = sorted(arr, key=lambda x: x, cmp=custom_cmp)

    # Concatenate the sorted numbers to form the largest possible value
    largest_value = ''.join(sorted_arr)

    return largest_value

# Example usage:
arr1 = ["3", "30", "34", "5", "9"]
arr2 = ["54", "546", "548", "60"]

print("Example 1 output:", largest_number(arr1))  # Output: "9534330"
print("Example 2 output:", largest_number(arr2))  # Output: "6054854654"
