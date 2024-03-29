# QUESTION 1
# ==========

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def simple_solution():
    count = 0
    for x in xrange(1, 1000):
        if not x % 3 or not x % 5:
            count += x
    return count

def one_liner():
    return sum([x for x in xrange(1, 1000) if not x % 3 or not x % 5])

print simple_solution()
print one_liner()