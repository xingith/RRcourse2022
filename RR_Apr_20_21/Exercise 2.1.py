## Exercise 2.1

#Write a function which takes *n* (float or integer) as a parameter and returns the largest Fibonacci number smaller than *n*. The function should be documented, with type hints, and appropriate comments.

t = input('please input a float or integer:')
t = float(t)
def Fibonacci(t):
    """Documentation

    Args:
        a,b fibonacci sequence with maximum number smaller than t.

    Returns:
        int: the largest Fibonacci number smaller than t.
    """
    a,b=1,1
    while b<t:
        a,b=b,a+b
    else:
        return a

print(Fibonacci(t))