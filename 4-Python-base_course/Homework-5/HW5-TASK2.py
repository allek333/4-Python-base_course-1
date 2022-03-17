'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.'''


with open('HW-5, task2.txt') as my_f:
    count = sum(1 for line in my_f)
    print(count)
'''похоже здесь нельзя октрыть большой файл. Он весь будет храниться
в памяти. В остальном работает.'''

# with open('hw5.txt', 'r+') as my_f:
#     string_number = 0
#     while string_number == my_f.readline() == True:
#         string_number =+ 1
#     else:
#         print(string_number)
# '''Этот код не делает цикл. Нет возврата к началу.'''
#
# with open('hw5.txt') as my_f:
#     line_count = 0
#     for line in my_f:
#         line_count =+ 1
#
#         print(line_count)
# '''показывает на каждой строке "1". Не суммирует'''
