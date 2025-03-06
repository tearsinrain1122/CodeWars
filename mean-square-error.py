# Complete the function that

# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair

# Solution
def solution(array_a, array_b):
    return sum([(array_a[i]-array_b[i])**2 if array_a[i]>array_b[i] else (array_b[i]-array_a[i])**2 for i in range(len(array_a))])/len(array_a)
