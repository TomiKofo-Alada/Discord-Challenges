# Write a python function that takes an integer n and returns the sume of all prime factors of n. If a 
# prime factor appears multiple times, include it that many times in the sum
# For example:
#     Input: n = 60
#     Output: 12 (since the prime factors of 60 are 2, 2, 3, and 5, and 2+2+3+5=10)
# Constraints:
#     n >=2

import math

def sum_prime(n):
    sum_factors = 0
    
    # do 2 first since 2 is the only even prime factoor
    while n % 2 == 0:
        sum_factors += 2
        n //= 2  # integer division
    
    # checking for odd factors starting from 3 up to sqrt(n) inclusive
    # stopped at sqrt(n) cuz any factor larger than sqrt(n) would  have already
    # been paired with a smaller factor since factor comes in pairs like 3*27 vs 9*9
    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        while n % factor == 0:
            sum_factors += factor
            n //= factor
            
    # if n is still > 2, then n is prime and needs to be added to the sum
    # this catches cases like 5,7,11 cuz it was not divisible 
    # by smaller primes(up to sqrt(n)) except itself 
    if n > 2:
        sum_factors += n
        
    return sum_factors
print(sum_prime(81))
print(sum_prime(60))
print(sum_prime(11))