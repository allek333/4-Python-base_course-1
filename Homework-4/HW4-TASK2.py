'''Представлен список чисел. Необходимо вывести
элементы исходного списка, значения которых
больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию,
оформить в виде списка. Для его формирования
используйте генератор.
Пример исходного списка:
[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].'''

number_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# my_sort_list = {el for el in number_list if number_list(el+1) > number_list(el)}
# TypeError: 'list' object is not callable
# my_sort_list = {el for el in enumerate(number_list) if [el+1] > [el]}
# TypeError: can only concatenate tuple (not "int") to tuple
# my_sort_list = {el for el in number_list if number_list{el+1} > number_list{el}}
# SyntaxError: invalid syntax
print(type(number_list))
print(type(my_sort_list))
