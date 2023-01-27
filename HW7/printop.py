def printOperationTable(operation, num_rows, num_columns):
  for i in range(1, num_rows + 1):
    print(*(operation(i, j) for j in range(1, num_columns +1 )))

f1 = lambda x, y: x * y
f2 = lambda x, y: x + y
f3 = lambda x, y: x - y
f4 = lambda x, y: x // y

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
print('\n Умножение')
printOperationTable(f1, n, m)
print('\n Сложение')
printOperationTable(f2, n, m)
print('\n Вычитание')
printOperationTable(f3, n, m)
print('\n Целочисленное деление')
printOperationTable(f4, n, m)

