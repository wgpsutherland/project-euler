# QUESTION 10
# ===========

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def is_prime(x):

    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False

    for i in xrange(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

print sum([x for x in xrange(0, 2000000) if is_prime(x)])
