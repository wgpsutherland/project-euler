# QUESTION 4
# ==========

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    num = str(n)
    return num == num[::-1]

palindromes = []

for i in xrange(999, 99, -1):
    for j in xrange(999, i, -1):
        product = i * j
        if is_palindrome(product):
            palindromes.append(product)

print max(palindromes)
