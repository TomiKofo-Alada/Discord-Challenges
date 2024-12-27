# Given an array of integers nums and an integer target,
# find two distinct indices in the array such that the 
# numbers at these indices add up to the target. 
# You need to return the indices as a list [index1, index2].
# Assume that there is exactly one solution, and you cannot
# use the same element twice.

# Input and Output Examples:
# -Example 1:
# Input:
# nums = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9, so the indices 0 and 1 are returned.
# -Example 2:
# Input:
# nums = [3, 2, 4]
# target = 6
# Output: [1, 2]
# Explanation: nums[1] + nums[2] = 2 + 4 = 6, so the indices 1 and 2 are returned.
# -Example 3:
# Input:
# nums = [3, 3]
# target = 6
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 3 + 3 = 6, so the indices 0 and 1 are returned.
# -Example 4:
# Input:
# nums = [1, 5, 7, 8]
# target = 12
# Output: [1, 3]
# Explanation: nums[1] + nums[3] = 5 + 8 = 12, so the indices 1 and 3 are returned.

def twosum(nums, target):
    # create a dictionary to store the index of each number
    nums_to_index = {}
    # loop through each number in the list
    for i, num in enumerate(nums):
        complement = target - num
        # check if complement is in dictionary
        if complement in nums_to_index:
            return [nums_to_index[complement], i]
        # store the current number's index in the dictionary
        
        nums_to_index[num] = i