# Basic list comprehension (1-5)
nums = [x for x in range(1, 6)]
print(nums)  # [1, 2, 3, 4, 5]

# With condition (even numbers 1-10)
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# if-else conditional
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}