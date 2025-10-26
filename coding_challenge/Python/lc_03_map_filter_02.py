""" `map` and `filter` are built-in Python functions that allow you to
    perform operations on iterable objects
    (e.g., lists, tuples) in a concise and functional manner.
    They are often used with lambda functions or regular functions to
    apply transformations and filters to the elements of an iterable."""

# map(function, iterable)    # Use map when you want to apply a specific function to each element.
# filter(function, iterable) # Use filter when you want to filter elements from an iterable based on a specific condition.


def square(x):
    return x**2


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5]

# squared = map(square, numbers)
# evens = filter(is_even, numbers)
squared = map(lambda x: x**2, numbers)
evens = filter(lambda x: x % 2 == 0, numbers)
squared_list = list(squared)
evens_list = list(evens)

print(squared_list)  # Output: [1, 4, 9, 16, 25]
print(evens_list)  # Output: [2, 4]


def 