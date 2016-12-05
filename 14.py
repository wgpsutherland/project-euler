# QUESTION 14
# ===========

# The following iterative sequence is defined for the set of positive integers:

    # n -> n/2 (n is even)
    # n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

    # 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

memoized = {1: 1}

def rule(n):
    return n / 2 if n % 2 == 0 else (n * 3) + 1

def len_chain(n):
    if n not in memoized:
        memoized[n] = 1 + len_chain(rule(n))
    return memoized[n]

longest_chain = 0
longest_chain_starting_num = 0

for x in xrange(1, 1000000):
    length = len_chain(x)
    if length > longest_chain:
        longest_chain = length
        longest_chain_starting_num = x

print longest_chain_starting_num, longest_chain
