# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    source_array_odd = [num for num in source_array if num%2==1]
    source_array_odd.sort()
    source_array = enumerate(source_array)
    for index,number in source_array:
        if number%2==0:
            source_array_odd.insert(index, number)
    return source_array_odd
