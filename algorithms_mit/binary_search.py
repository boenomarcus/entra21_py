"""
Binary Search Algorithm in Python

Author: Marcus Moresco Boeno
Date: 2020-06-10

Implements a function that gets the index of a given element in a list 
using the binary search algorithm as described on Chapter 2 of the 
book "Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def binary_search(A, num):
    """Binary Search algorithm
    
    > Arguments:
        - lst (list): List of numbers (needs to be sorted).
    
    > Output:
        - Index of the element (first occurrence, -1 if not found).
    """
    
    # Set initial state for bounds
    lower, upper = 0, len(A)-1
    
    # Iterate while there are chances to find search value
    while lower <= upper:

        # Calculate midpoint
        mid = (lower+upper)//2

        # Midpoint equals to search value
        if A[mid] == num:
            
            # Index is already at first list entry
            if mid == 0:
                return mid

            # Element to the left is not equal to the midpoint
            elif A[mid-1] != num:
                return mid
            
            # Element to the left is equal to the midpoint
            else:
                upper = mid - 1

        # Midpoint is smaller than search value
        elif A[mid] < num:
            lower = mid + 1

        # Midpoint is bigger than search value
        else:
            upper = mid - 1

    # Return -1 if search number not found
    return -1


if __name__ == "__main__":

    # Declare a list, sort it and present results for example purposes
    A = [-2, 2.4, 4, 4, 5, 6, 7, 7.5, 8, 9, 10]
    print("\n>> Binary Search Examples:")
    print(f"\nOriginal List: {A}")
    print(f"Index of -2: {binary_search(A, -2)}")
    print(f"Index of 4: {binary_search(A, 4)}")
    print(f"Index of 6: {binary_search(A, 6)}")
    print(f"Index of 7.5: {binary_search(A, 7.5)}")
    print(f"Index of 2.4: {binary_search(A, 2.4)}")
    print(f"Index of 10: {binary_search(A, 10)}")
    print(f"Index of 20: {binary_search(A, 20)}\n")