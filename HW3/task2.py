# ; Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# ; к заданному числу X. Пользователь в первой строке вводит натуральное число N 
# ; – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# ; Последняя строка содержит число X
# ; 5
# ; 1 2 3 4 5
# ; 6

# ; -> 5

n = int(input())
list = [int(input()) for i in range(n)]
# print(list) 
x = int(input())
differ = abs(list[0] - x)
res = list[0]
for i in range(1, len(list)):
    if abs(list[i] - x) < differ:
        differ = abs(list[i] - x)
        res = list[i]
print(res)
