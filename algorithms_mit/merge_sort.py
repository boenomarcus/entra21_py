"""
Merge Sort Algorithm in Python

Author: Marcus Moresco Boeno
Date: 2020-06-10

Implements a function that sorts a list of elements using the 
merge sort algorithm as described on Chapter 2 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def merge_sort(A):
    """Merge sort algorithm
    
    > Arguments:
        - lst (list): List of numbers to be sorted.
    
    > Output:
        - Sorted list on ascending order.
    """

    # Return the very list if only one element
    if len(A) == 1:
        return A
    else:

        # Find midpoint
        mid = len(A)//2

        # Recursively sort the two "main" halves
        a = merge_sort(A[:mid])
        b = merge_sort(A[mid:])

        # Create empty counters
        i = j = k = 0

        # Iterate over two halves
        while j < len(a) and k < len(b):

            if a[j] <= b[k]:
                A[i] = a[j]
                j += 1
            else:
                A[i] = b[k]
                k += 1
            i += 1
        
        # Correct last elements
        if j < len(a):
            A[i:] = a[j:]
        if k < len(b):
            A[i:] = b[k:]

        # Return results
        return A


if __name__ == "__main__":

    # Declare a list, sort it and present results for example purposes
    A = [6, 4, 5, 2.4, 7.5, 10, 7, 4, 9, 8,]
    print("\n>> Merge Sort Example:")
    print(f"\nOriginal List: {A}")
    print(f"Sorted List: {merge_sort(A)}\n")