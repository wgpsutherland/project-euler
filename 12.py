# QUESTION 12
# ===========

def factors(n):
    return set(reduce(list.__add__, [[x, n / x] for x in xrange(1, int(n ** 0.5) + 1) if n % x == 0]))

total = 0
for x in xrange(1, 100000000000000):

    total += x

    if len(factors(total)) > 500:
        print total
        break
