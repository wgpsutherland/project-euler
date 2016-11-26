# QUESTION 3
# ==========

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def is_prime(x):
    
    if x <= 2:
        return True

    if x % 2 == 0:
        return False

    for i in xrange(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

def is_factor(x, y):
    return y % x == 0

def largest_prime_factor(n):

    prime_factors = []

    for i in xrange(1, int(n ** 0.5) + 1):

        if is_factor(i, n):

            paired_factor = n / i

            if is_prime(i):
                prime_factors.append(i)

            if is_prime(paired_factor):
                prime_factors.append(paired_factor)

    return max(prime_factors)

print largest_prime_factor(600851475143)
