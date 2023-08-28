A = [1, 2, 3, 4, 5, 6]
B = [0, 0, 0, 0, 0, 0]

def f(n, k): # n은 인덱서, k는 상한
    global B
    if n >= k:
        print(B)
        return
    else:
        B[n] = A[n]
        f(n+1, k)

f(0, 6)        