def factorial(n):
    """ Computes the factorial of an integer.
    Type:
      factorial :: Number -> Number

    Raises:
      TypeError: n is not an integer
    """
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
