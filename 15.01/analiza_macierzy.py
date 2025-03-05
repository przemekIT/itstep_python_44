def process_matrix(matrix):
    # Funkcja sprawdzająca, czy macierz jest symetryczna względem głównej przekątnej
    def is_symetric(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True
    
    # Funkcja obliczająca sumę lementów na głównej przekątnej
    def diagonal_sum(matrix):
        return sum(matrix[i][i] for i in range(len(matrix)))
    
    # Funkcja tworząca nową macierz zgodnie z opisanym algorytmem
    def generate_new_matrix(matrix):
        n = len(matrix)
        # Obliczamy sume wierszy i kolumn
        row_sums = [sum(row) for row in matrix]
        col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]

        new_matrix = []
        for i in range(n):
            new_row = [] 
            for j in range(n):
                # Obliczamy nową wartość dla każdego elementu:
                # suma elementu macierzy, sumy wiersza i kolumny
                new_value = matrix[i][j] + row_sums[i] + col_sums[j]
                new_row.append(new_value)
            new_matrix.append(new_row)
        return new_matrix
    
    symmetric = is_symetric(matrix)
    diag_sum = diagonal_sum(matrix)
    new_matrix = generate_new_matrix(matrix)

    return symmetric, diag_sum, new_matrix

# Przykładowe dane wejściowe
matrix = [
    [1,2,3],
    [2,4,5],
    [3,5,6]
]

# Wywołanie funkcji i wypisanie wyników
result = process_matrix(matrix)
print("Czy macierz jest symetryczna?: ", result[0])
print("Suma elementów na głównej przekątnej: ", result[1])
print("Nowa macierz: ")
for row in result[2]:
    print(row)