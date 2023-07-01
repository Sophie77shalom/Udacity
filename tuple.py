def tuple_sum(tup):
    if len(tup) == 0:
        return 0
    else:
        return tup[0] + tuple_sum(tup[1:])

# Example tuple
tuplex = (4, 8, 3)

# Calling the function to get the sum of elements
result = tuple_sum(tuplex)
print("Sum of elements in the tuple:", result)
