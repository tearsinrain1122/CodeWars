# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same 
# value next to each other and preserving the original order of elements.

# Solution

def unique_in_order(sequence):
    if len(sequence)==0:
        return []
    list_unique = [sequence[0]]
    for i in range (1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            list_unique.append(sequence[i])
    return list_unique
