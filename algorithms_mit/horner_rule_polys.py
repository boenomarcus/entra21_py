"""
Horner's Rule to Evaluate Polynomials in Python

Author: Marcus Moresco Boeno
Date: 2020-10-07

Implements a function that evaluates a polynomial using the
Horner's Rule algorithm as described on Chapter 2 of the book 
"Introduction to Algorithms" by Thomas H. Cormen et al. (2009)

"""


def horner_eval(coeffs, x):
    """Horner Rule for Polynomial Evaluation
    
    > Arguments:
        - lst (list): List of ordered coefficients.
    
    > Output:
        - Polynomial evaluation for a given x.
    """

    # Iterate over coefficients
    i = len(coeffs)-1
    while i >= 0:
        if i == len(coeffs)-1:
            y = coeffs[i]
        else:
            y = coeffs[i] + x*y
        i -= 1
    
    # Return evaluation
    return y
    

if __name__ == "__main__":

    # Declare a list, sort it and present results for example purposes
    pol_coeffs = [-2310, 727, 382, -72, -8, 1,]
    print("\n>> Horner's Rule Example:")
    print(f"\nPolynomial Coeffs: {pol_coeffs}")
    print(f"Eval for p({2}): {horner_eval(pol_coeffs, 2)}")
    print(f"Eval for p({3}): {horner_eval(pol_coeffs, 3)}\n")