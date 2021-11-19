array = [1, 2, 4, 6, 5, 4, 2, 1]
array_2 = []
unique = [digit for digit in array if digit not in array_2]
print("Array:", *array)
print("Unique elements:", *unique)
