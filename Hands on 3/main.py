from batch import Batch

def transpose_matrix(matrix):
    # Obtener las dimensiones de la matriz original
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Inicializar la matriz transpuesta con ceros
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Calcular la transpuesta intercambiando filas por columnas
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

def matrix_multiply(A, B):
    # Verificar las dimensiones de las matrices
    if len(A[0]) != len(B):
        raise ValueError("Las dimensiones de las matrices no son compatibles para la multiplicación")
    
    # Inicializar la matriz resultante con ceros
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # Realizar la multiplicación de matrices
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

def inverse_matrix(matrix):
    # Obtener las dimensiones de la matriz
    n = len(matrix)
    
    # Inicializar la matriz identidad del mismo tamaño que la matriz original
    identity_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        identity_matrix[i][i] = 1
    
    # Concatenar la matriz original y la matriz identidad para formar una matriz aumentada
    augmented_matrix = [row + identity_matrix[i] for i, row in enumerate(matrix)]
    
    # Aplicar el método de eliminación de Gauss-Jordan
    for i in range(n):
        # Normalizar la fila i para que el elemento diagonal sea 1
        factor = augmented_matrix[i][i]
        for j in range(n * 2):
            augmented_matrix[i][j] /= factor
        
        # Eliminar los elementos por encima y por debajo del elemento diagonal
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(n * 2):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]
    
    # Extraer la matriz inversa de la parte derecha de la matriz aumentada
    inverse_matrix = [row[n:] for row in augmented_matrix]
    
    return inverse_matrix

batches = []

batches.append(Batch(108, 95))
batches.append(Batch(115, 96))
batches.append(Batch(106, 95))
batches.append(Batch(97, 97))
batches.append(Batch(95, 93))
batches.append(Batch(91, 94))
batches.append(Batch(97, 95))
batches.append(Batch(83, 93))
batches.append(Batch(83, 92))
batches.append(Batch(78, 86))
batches.append(Batch(54, 73))
batches.append(Batch(67, 80))
batches.append(Batch(56, 65))
batches.append(Batch(53, 69))
batches.append(Batch(61, 77))
batches.append(Batch(115, 96))
batches.append(Batch(81, 87))
batches.append(Batch(78, 89))
batches.append(Batch(30, 60))
batches.append(Batch(45, 63))
batches.append(Batch(99, 95))
batches.append(Batch(32, 61))
batches.append(Batch(25, 55))
batches.append(Batch(28, 56))
batches.append(Batch(90, 94))
batches.append(Batch(89, 93))

matrix_lin =[] 
for batch in batches:
    matrix_lin.append([1, batch.size])

matrix_cuadratic =[] 
for batch in batches:
    matrix_cuadratic.append([1, batch.size, batch.size ** 2])

matrix_cubic =[] 
for batch in batches:
    matrix_cubic.append([1, batch.size, batch.size ** 2, batch.size ** 3])

matrix_y = []
for batch in batches:
    matrix_y.append([batch.efficiency])

value = 105

#Lineal
transposed_matrix_lin = transpose_matrix(matrix_lin)
matrix_x_transposed = matrix_multiply(transposed_matrix_lin, matrix_lin)
inverse_lin = inverse_matrix(matrix_x_transposed)
matrixY_x_transposed = matrix_multiply(transposed_matrix_lin, matrix_y)

result_lin = matrix_multiply(inverse_lin, matrixY_x_transposed)

B0_lin = result_lin[0][0]
B1_lin = result_lin[1][0]

y_lin = B0_lin + B1_lin*value

print("ECUACION LINEAL:")
print("y = B0 + B1x")
print(f"y = {B0_lin} + ({B1_lin})({value})")
print(f"y = {y_lin}\n")

#cuadratica
transposed_matrix_cuadratic = transpose_matrix(matrix_cuadratic)
matrix_x_transposed_cuadratic = matrix_multiply(transposed_matrix_cuadratic, matrix_cuadratic)
inverse_cuadratic = inverse_matrix(matrix_x_transposed_cuadratic)
matrixY_x_transposed_cuadratic = matrix_multiply(transposed_matrix_cuadratic, matrix_y)

result_cuadratic = matrix_multiply(inverse_cuadratic, matrixY_x_transposed_cuadratic)

B0_cuadratic = result_cuadratic[0][0]
B1_cuadratic = result_cuadratic[1][0]
B2_cuadratic = result_cuadratic[2][0]

y_cuadratic = B0_cuadratic + B1_cuadratic*value + B2_cuadratic*(value**2)

print("ECUACION CUADRATICA:")
print("y = B0 + B1x + B2x^2")
print(f"y = {B0_cuadratic} + ({B1_cuadratic})({value}) + ({B1_cuadratic})({value**2})")
print(f"y = {y_cuadratic}\n")

#cubica
transposed_matrix_cubic = transpose_matrix(matrix_cubic)
matrix_x_transposed_cubic = matrix_multiply(transposed_matrix_cubic, matrix_cubic)
inverse_cubic = inverse_matrix(matrix_x_transposed_cubic)
matrixY_x_transposed_cubic = matrix_multiply(transposed_matrix_cubic, matrix_y)

result_cubic = matrix_multiply(inverse_cubic, matrixY_x_transposed_cubic)

B0_cubic = result_cubic[0][0]
B1_cubic = result_cubic[1][0]
B2_cubic = result_cubic[2][0]
B3_cubic = result_cubic[3][0]

y_cubic = B0_cubic + B1_cubic*value + B2_cubic*(value**2) + B3_cubic*(value**3)

print("ECUACION CUBICA:")
print("y = B0 + B1x + B2x^2 + B3x^3")
print(f"y = {B0_cubic} + ({B1_cubic})({value}) + ({B2_cubic})({value**2}) + ({B2_cubic})({value**3})")
print(f"y = {y_cubic}\n")