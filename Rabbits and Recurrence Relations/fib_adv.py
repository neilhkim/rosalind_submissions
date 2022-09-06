def fib(n, k):
    return fib(n-1, k) + k*fib(n-2, k) if n > 1 else 1

n, k = (int(i) for i in input().split())
print(fib(n,k))
