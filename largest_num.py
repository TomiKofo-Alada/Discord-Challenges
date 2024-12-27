# given a list of non-negative integers, arrange them such
# that they form the largest possible number

from functools import cmp_to_key


def largest_num(nums):
    nums = list(map(str, nums))
    def compare(a,b):
        return (1 if a + b > b + a else -1)
    
    nums.sort(key=cmp_to_key(compare), reverse=True)
    
    result = ''.join(nums)
    
    return '0' if result[0] == '0' else result

nums = [3, 30, 900, 34, 5, 7, 9]
print(largest_num(nums))