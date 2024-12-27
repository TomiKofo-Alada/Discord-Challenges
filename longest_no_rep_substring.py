# given a string, find the length of the longest substring
# that contains no repeating characters, also state the
# substring

def longest_no_rep(s):
    char_index_map = {} # tracks the most recent index of each character
    start = 0 # tracks the beginning of the substring window
    max_len = 0
    max_substring = ""
    
    for end in range(len(s)):
        current_char = s[end]
        
        # If the character is already in the window, move the start pointer
        if current_char in char_index_map and char_index_map[current_char] >= start:
            start = char_index_map[current_char] + 1
            
        # update the character\s latest index
        char_index_map[current_char] = end
        
        # update the max length and substring if we found a longer one
        window_len = end - start + 1
        if window_len > max_len:
            max_len = window_len
            max_substring = s[start:end + 1]
            
    return max_len, max_substring
            
s = "ahdbcisnsoasasbsssshdksisiiishanansjicdbchsusbbbbbshsaisiiduc"
print(longest_no_rep(s))
    