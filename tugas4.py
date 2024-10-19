A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
m, n = len(A), len(A[0])
p, q = len(B), len(B[0])
if n != p:
    print("Matriks tidak bisa dikalikan")
else:
    C = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(q)] for i in range(m)]
    for i in C:
        print(i)
