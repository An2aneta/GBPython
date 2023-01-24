# list1 = [i for i in range(0, 20)]
# print(list1)
# def f(x):
#     return x + 10

# #list1 = list(map(f, list1))
# list1 = list(map(lambda x: x + 10, list1)) # функция через lambda
# print(list1)


# list1 = [i for i in range(0, 20)]
# print(list1)
# res1 = list(filter(lambda x: x % 2 == 0, list1))
# print(res1)

# Функции высшего порядка

# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы 
# используется множество раз и вы не хотите ничего сломать): 
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# trasformation = lambda x: x

# values = [1, 23, 42, 'asdfg', True]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# 49. Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту,
#  по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей 
#  звезды таких планет нет, зато искусственные спутники были были запущены на круговые орбиты.
#   Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
#   Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
#    Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
#    При решении задачи используйте списочные выражения. 
#    Подсказка: проще всего будет найти эллипс в два шага: 
#    сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. 
#    Гарантируется, что самая далекая планета ровно одна
# Пример ввода и вывода данных представлены на следующем слайде

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод: 
# 2.5 10

# from math import pi
# def find_farthest_orbit(orbits):
#     orbits_temp = [i  for i in orbits if i[0] != i[1]]
#     orbits_s = [pi*i[0]*i[1] for i in orbits_temp]
#     orbits_s = 
#     max_index = orbits_s.index(max(orbits_s))
#     return orbits_temp[max_index]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# from math import pi

# def find_farthest_orbit(orbits):
#     #orbits_temp = [ i for i in orbits if i[0] != i[1]]
#     orbits_temp = list(filter(lambda x: x[0] != x[1], orbits))
#     #orbits_s = [ pi*i[0]*i[1] for i in orbits_temp]
#     orbits_s = list(map(lambda i: pi*i[0]*i[1], orbits_temp))
#     max_index = orbits_s.index(max(orbits_s))
#     return orbits_temp[max_index]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое 
# значение некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод:							Вывод:
# values = [0, 2, 10, 6]				same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)

def same_by(characteristic, objects):
    objects_temp = [characteristic(i) for i in objects]
    flag = True
    for i in range(len(objects_temp) - 1):
        if objects_temp[i] != objects_temp[i + 1]:
            flag = False
    return flag


values = [0, 2, 11, 6]	
if same_by(lambda x: x % 2 == 0, values):			
	print('same')
else:
 	print('different')