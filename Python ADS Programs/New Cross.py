def print_cross_string(input_str):
    length = len(input_str)
    mid = length // 2

    for i in range(length):

        for j in range(length):
            if i != j and i != length - j - 1:
                print(" ", end="")
            else:
                print(input_str[j], end="")
        print()

# Test the function with the example input
print_cross_string("LOVE2CODE")
