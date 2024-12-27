# write a function that takes a list of integers and moves
# all the zeros to the end, while maintaining the 
# relative order of the non-zero elements. you should do
# this in-place , meaning you can't 
# create a new list to solve the problem

def move_zeroes(nums):
    # initialize a pointer for the position of the next non-zero element
    non_zero_index = 0
    # move non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    # fill the rest of the list with zeros
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
            