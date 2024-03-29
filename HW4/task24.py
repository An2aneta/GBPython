# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
# – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
#  собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9


n = int(input())
list1 = [int(input()) for i in range(n)]
sumN0 = list1[len(list1) - 1] + list1[0] + list1[1]
sumNlast = list1[len(list1) - 2] + list1[len(list1) - 1] + list1[0]
# print(sumN0, sumNlast) 
if sumN0 > sumNlast:
    for i in range(1, n-1):
        if sumN0 < list1[i - 1] + list1[i] + list1[i + 1]:
            sumN0 = list1[i - 1] + list1[i] + list1[i + 1]
    print(sumN0)        
else:
    for i in range(1, n-1):
        if sumNlast < list1[i - 1] + list1[i] + list1[i + 1]:
            sumNlast = list1[i - 1] + list1[i] + list1[i + 1]
    print(sumNlast)