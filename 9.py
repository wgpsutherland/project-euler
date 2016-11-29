# QUESTION 9
# ==========

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    # a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_pythagorean_triplet(a, b, c):

    if not (a < b < c):
        return False

    return (a * a) + (b * b) == c * c

def triplet_sum_is_n(n):
    for a in xrange(0, n):
        for b in xrange(a + 1, n):

            c = n - a - b

            if c <= b:
                break

            if is_pythagorean_triplet(a, b, c):
                return a, b, c, a * b * c

print triplet_sum_is_n(1000)
