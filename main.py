'''
Решение задачи 1 предпроф. Экзамена
Программа читает данные из csv-файла
Создает новый файл с нужными значениями.
'''
from csv import reader, writer

with open('students.csv') as data_file:
    csv_data = reader(data_file, delimiter=',')
    for row in csv_data:
        if 'Хадаров Владимир' in row[1]:
            print(f'ты получил: {row[4]}, за проект {row[2]}')
