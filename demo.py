import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b!=0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    old_r, r = e, phi
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    if old_r != 1:
        return None  # No inverse
    return old_s % phi

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # standard choice
    if gcd(e, phi) != 1:
        raise ValueError("Choose different primes")
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

