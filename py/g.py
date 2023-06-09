import numpy as np  # импорт библиотеки numpy

# Входные данные
A = np.array([[-0.74, 0.47, -0.15, -0.3, 0.81],  # матрица коэффициентов системы уравнений
              [0.01, -0.65, -0.64, 0.58, -0.04],
              [-0.33, 0.01, -0.61, -0.95, 0.19],
              [-0.96, -0.42, -0.03, 0.68, -0.71],
              [0.07, 0.73, -0.97, 0.84, -0.35]])
B = np.array([-0.97, -0.86, -0.82, 0.99, -0.11])  # вектор свободных членов

# Метод Гаусса
n = len(B)  # размерность матрицы A
for i in range(n):  # цикл по i от 0 до n-1
    max_el = abs(A[i][i])  # выбираем максимальный элемент в i-ом столбце
    max_row = i
    for k in range(i+1, n):  # цикл по k от i+1 до n-1
        if abs(A[k][i]) > max_el:  # если в k-ой строке элемент в i-ом столбце больше, чем в i-ой строке
            max_el = abs(A[k][i])  # обновляем максимальный элемент
            max_row = k  # и запоминаем строку с этим элементом
    A[[i, max_row]] = A[[max_row, i]]  # меняем местами i-ую и max_row-ую строки матрицы A
    B[[i, max_row]] = B[[max_row, i]]  # меняем местами i-ый и max_row-ый элементы вектора B
    for k in range(i+1, n):  # цикл по k от i+1 до n-1
        div = A[k][i] / A[i][i]  # вычисляем коэффициент div
        A[k] -= div * A[i]  # вычитаем i-ую строку, умноженную на div, из k-ой строки матрицы A
        B[k] -= div * B[i]  # вычитаем i-ый элемент, умноженный на div, из k-го элемента вектора B

# Обратный ход
X = np.zeros(n)  # создаем нулевой вектор размерности n
for i in range(n-1, -1, -1):  # цикл по i от n-1 до 0 с шагом -1
    X[i] = (B[i] - np.dot(A[i][i+1:], X[i+1:])) / A[i][i]  # вычисляем i-ый элемент решения

# Вывод результата
print(X)  # выводим вектор решения