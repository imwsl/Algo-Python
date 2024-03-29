# Iteration and recursion
#

# Iteration
# for...loop

def for_loop(n: int) -> int:
    res = 0

    for i in range(1, n + 1):
        print("i -> ", i)
        res += i

    return res

print(for_loop(10))

# Iteration
# while

def while_loop(n: int) -> int:
    res = 0
    
    i = 1
    while i <= n:
        res += i
        i += 1
    return res

print(while_loop(10))

# recursion
# 

def recur(n: int) -> int:
    if n <= 1: 
        return 1
    return n + recur(n - 1)

print(recur(10))

# tail recursion
#

def tail_recur(n, res):
    if n <= 0:
        return res 
    return tail_recur(n - 1, n + res)

print(tail_recur(10, 0))

# fib
# [0, 1, 1, 2, 3, 5, 8....]
def fib(n: int) -> int:
    if n <= 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(4))

##
## iteration: simple loop, task...
## recursion: tree, graphs, divide-and-conquer, backtracking...