"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print('Second element of a: ', a[1])

# Output the second-to-last element: 9
print('Second to last element of a: ', a[-2])

# Output the last three elements in the array: [7, 9, 6] 
print('Last 3 elements of a: ', *a[-3:])

# Output the two middle elements in the array: [1, 7]
print('middle two elements of a: ', *a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print('Print all except first: ', *a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print('Print all except last: ', *a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print('print letters 8-12: ', s[7:12])
