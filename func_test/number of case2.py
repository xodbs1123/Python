L = [0, 0, 0]

def f(n, k, m):
    if n == k:
        print(L)
    else:
       
        for i in range(m):
            L[n] = i
            f(n + 1, k, m)
            
f(0, 3, 5)