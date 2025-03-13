# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# Solution

def move_zeros(lst):
    no_zeros = lst.count(0)
    new_lst = [number for number in lst if number!= 0]
    for i in range(no_zeros):
        new_lst.append(0)
    return new_lst
