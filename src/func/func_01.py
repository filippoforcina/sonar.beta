
# se il resto di n/2 è 0, n è pari
def is_even(n):
    """Return True if n is even, False otherwise."""
    if n%2 == 0:
        return True
    else:
        return False

help(is_even)

print (is_even(4))
#True
print (is_even(5))
#False
print(is_even(-7))
#False
