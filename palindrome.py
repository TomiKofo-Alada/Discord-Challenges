# Write a python function that takes a string s as input and returns the longest palindromic substring in s. A palindromic substring that reads the same forward and backward. 
# If there are multiple palindromic substrings with the same maximum length, return the first one that appears in the sstring
# input: a string s (1<=len(s)<= 1000) which contains only lowercase and uppercase english letters
# output: a string representing the longest palindromic substring in sum


def palindrome(s: str) -> str:
    # Helper function to expand around center and return the longest palindrome length and positions
    def expand_around_center(left: int, right: int) -> (int, int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return start and end indices of palindrome
        return left + 1, right - 1

    start, end = 0, 0  # To store the start and end of the longest palindromic substring

    for i in range(len(s)):
        # Odd-length palindromes (single character center)
        left1, right1 = expand_around_center(i, i)
        
        # Even-length palindromes (center between two characters)
        left2, right2 = expand_around_center(i, i + 1)
        
        # Choose the longer of the two palindromes found
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    # Extract and return the longest palindromic substring
    return s[start:end + 1]

    