import pandas

total = int(input('введите колчество приборов'))
xls_file = 'май проект 296шт.xls'
first_number = input('ведите первый номер прибора')
#file_open = "General_file.txt"

exel_date = pandas.read_excel(xls_file, sheet_name='Набор номеров')
list_date = exel_date[first_number].tolist()


def readlist(file):
    file = open(file, 'r', encoding='utf-8')
    line = file.read()
    return line


with open("General_file.txt", 'a', encoding='utf-8') as f:
    if readlist("General_file.txt").count(first_number) >= 1:
        with open('Duplicate_numbers.txt', 'a', encoding='utf-8') as file:
            file.write(first_number + ' ')
    else:
        f.write(first_number + ' ')


with open('Duplicate_numbers.txt', 'w', encoding='utf-8') as file:
    file.write('')

with open("General_file.txt", 'a', encoding='utf-8') as f:
    for i in range(total-1):
        if readlist("General_file.txt").count(str(list_date[i])) >= 1:
            with open('Duplicate_numbers.txt', 'a', encoding='utf-8') as file:
                file.write(str(list_date[i]) + ' ')
            print(f'{list_date[i]} такой номер уже есть')
        else:
            f.write(str(list_date[i]) + ' ')