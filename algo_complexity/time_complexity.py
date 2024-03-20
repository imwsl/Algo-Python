# time_complexity.py
#

def algo_a(n: int):
    print(n)                # O(1)
    
def algo_b(n: int):
    for _ in range(n):
        print(0)            # O(n)

def algo_c(n: int):
    for _ in range(100000):
        print(0)            # O(n), same as algo_c


# O is big-O notation
# T(n) = 3 + 2n = O(n)
#

# O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)
# 
# 

# O(1)
# example
def constant(n: int) -> int:
    count = 0
    size = 10000
    for _ in range(size):
        