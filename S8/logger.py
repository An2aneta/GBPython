def input_data():
    pass

def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first = file.readlines()
        data_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or data_first[i] == len(data_first) - 1:
                data_second.append(''.join(data_first[j:i+1]))
                j = i
            print(''.join(data_second))

def put_data():

def delete_data():
