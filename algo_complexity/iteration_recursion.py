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