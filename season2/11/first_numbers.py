
# from time import sleep
from math import sqrt
from multiprocessing import Pool

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3,int(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def calculate_prime_range(start,end):
    if start % 2 == 0:
        start += 1
    return [n for n in range(start ,end) if is_prime(n)]

def primes(n , p):
    segment_size = n // p
    segments = []
    for i in range(p):
        start = i * segment_size if i > 0 else 3
        end = (i+1) * segment_size if i != p-1 else n
        segments.append((start , end))
    with Pool(processes=p) as pool:
        r = pool.starmap(calculate_prime_range , segments)    
    result = [2]
    for p in r:
        result.extend(p)
    return result

N = 100
P = 1
prime_numbers = primes(N , P)
print(prime_numbers)

