# given an integer array nums, find the subarray with the largest sum and return its sum
# ex 1
# input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# output:6
# explanation: the subarray [4,-1,2,1] has the largest sum 6
# ex 2
# input: nums=[1]
# output: 1
# explanation: the subarray [1] has the largest sum 1
# ex 3
# input: nums = [5,4,-1,7,8]
# output: 23
# explanation: the subarray [5,4,-1,7,8] has the largest sum 23
# constraints: 1<=nums.length<=10^5
# -10^4 <= nums[i] <= 10^4

def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        # update the current sum to be the max of the starting fresh at num or adding num to current sum
        current_sum = max(num, current_sum + num)
        # update max sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    return max_sum
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))
    
    