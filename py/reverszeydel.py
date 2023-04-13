import numpy as np

# Входные данные
A = np.array([[-1,-1,-1,-2], 
              [2,3,4,3], 
              [-2,0,1,-6], 
              [-2,-2,-3,-3]])

# Размерность матрицы
n = A.shape[0]

# Создание матриц L и U
L = np.zeros((n,n))
U = np.zeros((n,n))

# LU-разложение
for j in range(n):
    L[j][j] = 1.0
    for i in range(j+1):
        s = sum(U[k][j] * L[i][k] for k in range(i))
        U[i][j] = A[i][j] - s
    for i in range(j, n):
        s = sum(U[k][j] * L[i][k] for k in range(j))
        L[i][j] = (A[i][j] - s) / U[j][j]

# Решение систем уравнений Ly = I и Ux = y для получения столбцов обратной матрицы
inv_A = np.zeros((n,n))
I = np.eye(n)
for k in range(n):
    # Решение системы уравнений Ly = I для y
    y = np.zeros((n,1))
    for i in range(n):
        s = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (I[i][k] - s) / L[i][i]
    
    # Решение системы уравнений Ux = y для x
    x = np.zeros((n,1))
    for i in range(n-1, -1, -1):
        s = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = (y[i] - s) / U[i][i]
    
    # Сохранение результата в обратную матрицу
    for i in range(n):
        inv_A[i][k] = x[i][0]

# Вывод результата
print("Обратная матрица:")
print(inv_A)