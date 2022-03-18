'''Создать текстовый файл (не программно). Построчно
записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести
фамилии этих сотрудников. Выполнить подсчёт средней величины
дохода сотрудников.'''

with open('hw5-task3.txt', 'r+', encoding='UTF8') as my_f:
    line_num = []
    for line in my_f.readlines():
        # print(type(line))
        line_s = line.split()
        # print(line_s)
        # print(type(line_s))
        for i, num in enumerate(line_s):
            if float(num[',','end']) < 20000:
            # float(num)
            #     continue
            # print(type(num))

                line_num.append(str(num['start',',']))
        # print(type(num))
        # print(line_s)
        # print(line)
#
# with open('hw5-task3.txt', 'r+', encoding='UTF8') as my_f:
#     line_num = []
#     for line in my_f.readlines():
#         # print(type(line))
#         line_s = str(line.split())
#         # print(type(line_s))
#         for num in line_s:
#             if num.isnumeric() and int(num) < 20000:'''
#               здесь логическое И не сработало, не
#                 сортирует значения'''
#                 line_num.append(float(num))
#         # print(type(num))
#         # print(line_s)
#         print(line)
#
# with open('hw5.txt', 'r+', encoding='UTF8') as my_f:
#     for line in my_f.readlines():
#         try:
#             int(line.split) < 10000
#         except ValueError:
#             pass
#     print(line)

# with open('hw5.txt', 'r+', encoding='UTF8') as my_f:
#     num_list = my_f.writelines()
#     for line in num_list.split():
#         if num_list.isnumeric():
#
# with open('hw5-task3.txt', 'r+', encoding='UTF8') as my_f:
#     line_num = []
#     for line in my_f.readlines():
#         print(type(line))
#         line_s = str(line.split())
#         print(type(line_s))
#         if word in line_s.isdigit(): # .isdigit и .isnumeric
#         #используется только к строкам
#         '''Traceback (most recent call last):
#   File "C:/Users/Alek/AI_2022_Geekbrains/4-Python-base_course/Homework-5/test.py", line 26, in <module>
#     if word in line_s.isdigit(): # .isdigit и .isnumeric
# NameError: name 'word' is not defined'''
#             line_num.append(float(line_s))
#         print(type(word))
#         print(line_s)
#         print(line)
