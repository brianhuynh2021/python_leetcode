


def count_drops(array):
    dropCount = 0
    foundB = False  # Flag to indicate we've started finding B's
    for char in array:
        if char == 'B':
            foundB = True
        elif char == 'A' and foundB:
            # If we find an A after finding a B, we need to drop it
            dropCount += 1
    return dropCount


# Example usage
input_string = "AABBAABBAABB"
dropped_chars = count_drops(input_string)
print("Number of characters to drop:", dropped_chars)
