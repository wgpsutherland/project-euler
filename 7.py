# QUESTION 7
# ==========

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def is_prime(x):
    
    if x <= 2:
        return True

    if x % 2 == 0:
        return False

    for i in xrange(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

num_primes = 0
largest_prime = 0
count = 2
while num_primes < 10001:

    if is_prime(count):
        largest_prime = count
        num_primes += 1

    count += 1

print largest_prime
