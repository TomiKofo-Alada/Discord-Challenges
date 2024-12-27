# write a python function called odd_squares_sum that takes
# a single integer n as input. the function should return 
# the sum of the squares of all odd numbers from 1 to n 
# (inclusive). however the twist is that if the sum exceeds 1000,
# you should return the string "too large" instead of the sum

def odd_squares(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i ** 2
        if total > 1000:
            return "too large"
    return total
    
        