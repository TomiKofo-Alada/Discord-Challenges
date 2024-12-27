# write a function that finds the 2nd largest number in a list of integers.
# what happens if the list has duplicates or only one unique element

nums = [1, 99, 7, 8, 78, 36, 745]
def second_largest(nums):
    #remove duplicates by converting list to a set
    unique_nums = set(nums)
    # check if there are fewer than 2 unique elements
    if len(unique_nums) < 2:
        return None
    #sort set and return the 2nd largest num
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums[1]

# alternative for optimal performance:avoid sorting
def second_largest_alt(nums):
    unique_nums = set(nums)
    if len(unique_nums) < 2:
        return None
    # initializae the 2 largest elements
    first, second = float('-inf'), float('-inf')
    
    for num in unique_nums:
        if num > first:
            second = first
            first = num
        elif num > second:
            second = num
    return second

print(second_largest(nums))
print(second_largest_alt(nums))