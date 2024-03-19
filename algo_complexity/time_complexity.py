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

