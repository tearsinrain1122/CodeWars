# You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.

# If there is no index that would make this happen, return -1.

# Solution

def find_even_index(arr):
    print(arr)
    for i in range(0,len(arr)-1):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    if sum(arr[:len(arr)-1]) == 0:
        return len(arr)-1
    return -1
