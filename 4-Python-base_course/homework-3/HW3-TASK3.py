'''Реализовать функцию my_func(), которая принимает
три позиционных аргумента и возвращает сумму наибольших
двух аргументов.'''

def my_func():
    lst = list(input(''.split()))
    maximum = lst.pop()
    maximum2 = lst.pop()
    for i in lst:
        if i > maximum:
            maximum2 = maximum
            maximum = i
        elif i > maximum2:
            maximum2 = i
print(my_func())
print(my_func())
print((max(my_func()+((max-1)(my_func())))))
'''Здесь решение так и не смог докрутить. Где-то
запутался в методах. Ниже правильное решение'''

'''Всё что приходит надо перевести в лист.
Затем метод .pop удаляет указанный индекс:
    - в листе метод .index ищет минимальное значение
    - найденный индекс элемента удаляется методом .pop
return возвращает сумму

def my_func(num_1, nim_2, num_3):
    try:
        my_list = [num_1, nim_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'


print(my_func(1, 2, 3))'''
