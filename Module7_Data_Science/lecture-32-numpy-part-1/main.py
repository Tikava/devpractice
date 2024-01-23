import numpy as np

matrix1 = np.random.randint(1, 10, size=(3, 3))
matrix2 = np.random.randint(1, 10, size=(3, 3))

result_matrix = np.multiply(matrix1, matrix2)
print(matrix1)
print(matrix2)
print(result_matrix)
sum = np.sum(result_matrix)
print('Sum:', sum)


data = np.random.randint(1, 10, size=100)
print('Avg', np.average(data))
print('Median', np.median(data))
print('SD', np.std(data))