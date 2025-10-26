"""`map` and `filter` are built-in Python functions that allow you to
perform operations on iterable objects
(e.g., lists, tuples) in a concise and functional manner.
They are often used with lambda functions or regular functions to
apply transformations and filters to the elements of an iterable."""

# map(function, iterable)    # Use map when you want to apply a specific function to each element.
# filter(function, iterable) # Use filter when you want to filter elements from an iterable based on a specific condition.


def square(x):
    return x**2


numbers = [1, 5, 14, 11, 23, 4]

# for num in numbers:
#     result = square(num)
#     print(result, end=' ')

result = map(lambda x: x**2, numbers)
# print(list(result))

square_values = list(result)
print(square_values)
even_number = filter(lambda x: x % 2 == 0, square_values)
print(list(even_number))
