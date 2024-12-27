# Given two sorted arrays, X[] and Y[] of size m and n each, merge elements of X[] with elements of array Y[] by maintaining the sorted order, i.e., fill X[] with the first m smallest elements and fill Y[] with remaining elements.

# Do the conversion in-place and without using any other data structure.

#  For example,

# Input:     X[] = { 1, 4, 7, 8, 10 }      Y[] = { 2, 3, 9 } 
# Output: X[] = { 1, 2, 3, 4, 7 }        Y[] = { 8, 9, 10 }

def sorted_array(X, Y):
    m = len(X)
    n = len(Y)
    
    # traverse every element in X
    for i in range(m):
        if X[i] > Y[0]:
            X[i], Y[0] = Y[0], X[i]
            # resort Y so that it remains sorted after the swap
            # only need to sort y[0] up to the right place since the rest is already sorted
            first = Y[0]
            k = 1
            while k < n and Y[k] < first:
                Y[k - 1] = Y[k]
                k += 1
            Y[k - 1] = first
    return X, Y
            
X = [1, 4, 7, 8, 10]
Y = [2, 3, 9]
print(sorted_array(X, Y))
