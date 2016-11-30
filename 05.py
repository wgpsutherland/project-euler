# QUESTION 5
# ==========

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)

track = 1
for i in xrange(1, 21):
    track = lcm(track, i)
print track
