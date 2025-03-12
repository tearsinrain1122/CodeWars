# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n 
# raised to consecutive powers starting from p is equal to k * n.

# Solution
def dig_pow(n, p):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])**(i+p)
    if sum % n == 0:
        return sum/n
    return -1
