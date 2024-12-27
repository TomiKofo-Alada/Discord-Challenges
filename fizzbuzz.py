# Imagine you have a list of numbers, starting from 1 and 
# going up to a certain number, say 100. For each number
# in this list, we’ll use some simple rules to decide 
# what to print out:

# If the number is divisible by 3, we’ll print "Fizz".
# If the number is divisible by 5, we’ll print "Buzz".
# If the number is divisible by both 3 and 5, we’ll print "FizzBuzz".
# If the number is not divisible by 3 or 5, we’ll just print the number itself.
# So, for example:

# For the number 1, we print "1".
# For the number 3, we print "Fizz".
# For the number 5, we print "Buzz".
# For the number 15, we print "FizzBuzz".

def fizz_buzz(max):
    for num in range(1, max + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
            
fizz_buzz(100)