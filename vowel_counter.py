# write a python function to count the number of vowels in a given string. for simplicity, consider the vowels to be a, e,i,o,u(both uppercase and lowercase)
# the function should be case insensitive, meaning it should count both uppercase and lowercase vowels equally

def vowel_counter(s):
    s = s.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = " Hello World"
print(vowel_counter(s))