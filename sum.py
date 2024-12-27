# Write a function called number_sum(n) that adds up all the numbers from 1 to n. For example:

# number_sum(5) -> 1+2+3+4+5 -> 15

# number_sum(3) -> 1+2+3 -> 6

def number_sum(n):
    total = 0
    
    for i in range(1, n + 1):
        total += i
    return total

def number_sum_alt(n):
    return n * (n + 1) // 2

n = 100
print(number_sum(n))
print(number_sum_alt(n))