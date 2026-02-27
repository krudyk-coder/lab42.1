import math


def get_fact(x):
    return math.factorial(x)

def nsd(x,y):
    return math.gcd(x, y)

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
             return False
    return True
