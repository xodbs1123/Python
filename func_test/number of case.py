L = [0, 0, 0,]

def f(n, k):
    if n == k:
        print(L)
    else:
        # L[n] = 0
        # f(n + 1, k)
        # L[n] = 1
        # f(n + 1, k)
        for i in range(2):
            L[n] = i
            f(n + 1, k)
            
f(0, 3)

