"""
Bubble Sort Algorithm in Python

Author: Marcus Moresco Boeno
Date: 2020-06-10

Implements a function that sorts a list of elements using the 
bubble sort algorithm as described on Chapter 2 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def bubble_sort(A):
    """Bubble sort algorithm
    
    > Arguments:
        - lst (list): List of numbers to be sorted.
    
    > Output:
        - Sorted list on ascending order.
    """

    # Iterate over list elements (n-1 because the last element
    # will be sorted when the others already are)
    for i in range(len(A)-1):
        
        # Iterate over elements that are not sorted yet
        # j >= i+1 will guarantee that elements positioned
        # on the left (already sorted) will not be misplaced
        j = len(A)-1
        while j >= i+1:
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            j -= 1
    
    # Return sorted list
    return A

if __name__ == "__main__":

    # Declare a list, sort it and present results for example purposes
    A = [6, 4, 5, 2.4, 7.5, 10, 7, 4, 9, 8,]
    print("\n>> Bubble Sort Example:")
    print(f"\nOriginal List: {A}")
    print(f"Sorted List: {bubble_sort(A)}\n")