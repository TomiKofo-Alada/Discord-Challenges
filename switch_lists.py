# instructions:
# You are given a list of  integers with an even length of numbers e.g:[2,3,1,2,2,4]

# your task is to switch the positions of each pair of integers in the list and return it:
# eg:
# Input:[2,3,4,6,2,2]
# output:[3,2,6,4,2,2]

# Input:[4,5]
# Output:[5,4]

def switch_lists(nums):
    # loop through the list in steps of 2 to swap pairs
    for i in range(0, len(nums), 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

nums = [1, 2, 3, 4 , 5, 6, 7, 8]
print(switch_lists(nums))
        