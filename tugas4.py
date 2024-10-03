

# Fungsi untuk perkalian matriks
def multiply_matrices(A, B):
    # Dapatkan ukuran matriks A dan B
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])
    
    # Cek apakah matriks dapat dikalikan
    if n != p:
        return "Matriks tidak dapat dikalikan"
    
    # Buat matriks hasil C dengan ukuran m x q
    C = [[0 for _ in range(q)] for _ in range(m)]
    
    # Lakukan perkalian matriks
    for i in range(m):
        for j in range(q):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

# Contoh input matriks A dan B dengan ukuran 3x3
A = [
    [3,4,5],
    [2,2,1],
    [2,3,7]
]

B = [
    [3,7,6],
    [8,9,9],
    [2,2,2,]
]

# Cetak hasil perkalian
hasil = multiply_matrices(A, B)
print(hasil)
