"""
n = 5
Print the integer 12345
"""

# Print the list of integers from 1 through n as a string, without spaces.
n = int(input())
# create list
l=range(n + 1)
# create string by concatenating objects in list
num = ''.join(str(i) for i in l)
# convert string to int
z = int(num)

print(z)
    
