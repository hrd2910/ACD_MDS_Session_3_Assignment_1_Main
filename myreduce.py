#  Write a Python Program to implement your own myreduce() function which works exactly
#  like Python's built-in function reduce()

def myreduce(fnc, seq):
    count = seq[0]
    for next in seq[1:]:
        count = fnc(count, next)
    return count

myreduce( (lambda x, y: x + y), [1, 2, 3, 4, 5])



