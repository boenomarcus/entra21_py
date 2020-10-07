"""
Selection Sort Algorithm in Python

Author: Marcus Moresco Boeno
Date: 2020-10-06

Implements a function that sorts a list of elements using the 
selection sort algorithm as described on Chapter 2 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def selection_sort(A):
    """Selection sort algorithm
    
    > Arguments:
        - lst (list): List of numbers to be sorted.
    
    > Output:
        - Sorted list on ascending order.
    """
    # Iterano over n-1 elements
    for i in range(len(A)-1):
        
        # Start comparison on the first non-sorted position
        k = i
        
        # Update index of smallest non-sorted element
        for j in range(i+1, len(A)):
            if A[j] < A[k]:
                k = j
        
        # Update list with sorted elements to the left
        A[i], A[k] = A[k], A[i]
    
    # Return sorted list
    return A

if __name__ == "__main__":

    # Declare a list, sort it and present results for example purposes
    A = [6, 4, 5, 2.4, 7.5, 10, 7, 4, 9, 8,]
    print("\n>> Selection Sort Example:")
    print(f"\nOriginal List: {A}")
    print(f"Sorted List: {selection_sort(A)}\n")