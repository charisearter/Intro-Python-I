# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(is_even(6))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
even = is_even(num)
if even == False:
    print('Odd')
else:
    print('Even!')
