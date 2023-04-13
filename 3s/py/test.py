import numpy as np

# задаем коэффициенты системы уравнений
A = np.array([[25, 4, 7, -3, -1],
              [-8, 42, 8, -9, -3],
              [-6, 4, 34, 4, -8],
              [-8, 4, 7, 36, 9],
              [6, -6, -2, -4, -29]])
b = np.array([32, 60, 84, 96, 23])

# задаем начальное приближение x0
x0 = np.zeros(len(b))

# задаем максимальное число итераций и желаемую точность решения
max_iterations = 100
tolerance = 1e-6

# выполняем итерации
for i in range(max_iterations):
    x1 = np.zeros(len(b))
    for j in range(len(b)):
        s = 0
        for k in range(len(b)):
            if k != j:
                s += A[j,k] * x0[k]
        x1[j] = (b[j] - s) / A[j,j]
    if np.allclose(x0, x1, rtol=tolerance):
        break
    x0 = x1

# выводим решение
print("Solution:", x1)