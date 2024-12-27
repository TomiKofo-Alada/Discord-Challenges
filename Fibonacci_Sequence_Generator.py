# Write a Python function that generates the first n numbers in the Fibonacci sequence, where n is a 
# positive integer provided as input. The Fibonacci sequence is defined as follows:
#     F(0) = 0
#     F(1) = 1
#     For n >= 2, F(n) = F(n-1) + F(n-2)
# Example:
#     Input: n= 7
#     Output: [0,1,1,2,3,5,8]

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0,1]
    
    for i in range(2,n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    
    return sequence


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(8))