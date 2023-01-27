from logger import input_data

def interface():
    print('Добрый день! Это бот-помощник. \n'
    'Что вы хотите сделать? \n'
    '1 - записать данные\n'
    '2 - вывести данные\n'
    '3 - изменить данные\n'
    '4 - удалить данные\n')

    command = int(input("Ваш выбор: "))
    while command < 1 or command > 4:
        command = int(input("Еще один шанс! Ваш выбор: "))

if command == 1:
    input_data()
elif command == 2:
    print_data()
elif command == 3:    
    put_data()
else: delete_data()