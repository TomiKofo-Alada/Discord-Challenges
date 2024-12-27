# write a function called unique elements that takes a list of integers and returns
# a new list containing only unique elements, in the order they 1st appeared. 
# you may not use any built in function that directly  removes duplicates like set


def unique_elements(lst:list) -> list:
    unique_lst = []
    
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst