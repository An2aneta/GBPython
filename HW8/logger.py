from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 Вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 Вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варината: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('Успешно!!')


# def print_data(fileNumberber = None):
    
#     if fileNumberber is None or fileNumberber == 1:
#         print('1 файл:')
#         with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
#             data_first = file.readlines()
#             data_first_second = []
#             j = 0
#             num = 1
#             for i in range(len(data_first)):
#                 if data_first[i] == '\n' or i == len(data_first) - 1:
#                     data_first_second.extend([f"\n{num}.\n", ''.join(data_first[j:i]).strip(), '\n'])
#                     j = i
#                     num += 1
#             data_first = data_first_second
#             print(''.join(data_first))
    
#     if fileNumberber is None or fileNumberber == 2:
#         print('2 файл:\n')
#         with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
#             data_second = list(file.readlines())
#             num = 1
#             for i in data_second:
#                 if i != '\n':
#                     i = i.strip()
#                     print(f'{num}. {i}')
#                     num += 1       


def print_data(fileNumber):
    if fileNumber is None or fileNumber == 1:
        print('1 файл:\n')
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            data_first = file.readlines()
            data_first_second = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_second.append(''.join(data_first[j:i]))
                    j = i
            data_first = data_first_second
            print(''.join(data_first))
        return data_first    


    if fileNumber is None or fileNumber == 2:
        print('2 файл:\n')
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            data_second = list(file.readlines())

            print(*data_second)
    
        return data_second



def put_data():
    # data_first, data_second = print_data()
    fileNumber = int(input(f'Укажите какой файл нужно изменить:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))
    
    if fileNumber != 1 and fileNumber != 2:
        fileNumber = int(input(f'Укажите какой файл нужно изменить:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()

    if fileNumber == 1:
        data_first = print_data(1)
        print_data(1)
        nRec = int(input('\nВведите номер записи, которую нужно изменить: '))
        while nRec > len(data_first):
            nRec = int(input("Введенное число больше, чем количество записей! Try again: "))
        if nRec == 0:  
            data_first = [f'{name}\n{surname}\n{phone}\n{adress}\n'] + data_first[nRec+1:]
        else:
            data_first = data_first[:nRec] + [f'\n{name}\n{surname}\n{phone}\n{adress}\n'] + data_first[nRec+1:]  
        print(data_first)
             
        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            file.writelines(i for i in data_first)
            file.write('\n')
        print('Успешно!!')           

    if fileNumber == 2:
        data_second = print_data(2)
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            nRec = int(input('\nУкажите номер записи, которую Вы хотите изменить: '))
            while nRec > len(data_second):
                nRec = int(input("Введенное число больше, чем количество записей! Try again: "))
            if nRec == 0:
                data_second = [f'{name};{surname};{phone};{adress}\n'] + data_second[nRec + 1:]
            elif nRec == 1:  
                data_second = data_second[:nRec + 1] + [f'{name};{surname};{phone};{adress}\n'] + data_second[nRec + 2:]
            elif nRec == len(data_second):
                data_second = data_second[:nRec + nRec] + [f'{name};{surname};{phone};{adress}\n\n']
            else:      
                data_second = data_second[:nRec + nRec] + [f'{name};{surname};{phone};{adress}\n\n'] + data_second[nRec + nRec + nRec:]
            for i in data_second:
                file.write(i)
        print('Успешно!!')   


def delete_data():
    fileNumber = int(input(f'В каком файле нужно удалить запись?:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))
    
    if fileNumber!= 1 and fileNumber != 2:
        fileNumber = int(input(f'Укажите в каком файле Вы хотите удалить запись:\n'
                        f'1 - 1 файл\n'
                        f'2 - 2 файл\n'))

    if fileNumber == 1:
        print_data(1)
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            nRec = int(input('\nКакой номер записи, нужно удалить: '))
            data_first = file.readlines()
            new_data_first = []
            count = 0
            i = 0
            while i < len(data_first):
                if count != nRec:
                    if data_first[i] != '\n':
                        new_data_first.append(f'{data_first[i]}')
                        i += 1
                    else:
                        new_data_first.append('\n')
                        count += 1
                        i += 1
                else:
                    count += 1
                    i += 5
                
        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_data_first:
                file.write(i)

    if fileNumber == 2:
        print_data(2)
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            nRec = int(input('\nКакой номер записи, нужно удалить: '))
            data_second = file.readlines()
            new_data_second = []
            count = 0
            i = 0
            while i < len(data_second):
                if count != nRec:
                    if data_second[i] != '\n':
                        new_data_second.append(f'{data_second[i]}')
                        i += 1
                    else:
                        new_data_second.append('\n')
                        count += 1
                        i += 1
                else:
                    count += 1
                    i += 2
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_data_second:
                file.write(i)

