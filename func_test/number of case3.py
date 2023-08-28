C = [0, 0, 0, 0, 0]
U = [1, 2, 3, 4, 5]
A = [0, 0, 0, 0, 0]

def f(n, k, m):
    if n >= k:
        print(A)
    
    else:
        for i in range(m):
            if C[i] == 0:
                C[i] = 1
                A[n] = U[i]
                f(n+1, k, m)
                C[i] = 0

f(0, 5, 5)