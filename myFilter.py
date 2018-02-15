#Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()

def even(X):
    if not X % 2:
        return True
    return False

def myFilter(f, L):
    return [x for x in L if f(x)]

myFilter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # Filtering even numbers