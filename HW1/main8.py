# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
#  отломить k долек, если разрешается сделать один разлом по прямой 
#  между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print("Введите первый размер шоколадки:")
n = int(input('n = '))
print("Введите второй размер шоколадки:")
m = int(input('m = '))
print("Введите количество долек:")
k = int(input('k = '))

if k > n or k > m:
    if k % n == 0 or k % m == 0:
        print("Возможно отломить")
    else:
        print("Невозможно отломить")
else:
     print("Невозможно отломить") 