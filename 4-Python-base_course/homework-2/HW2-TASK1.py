'''Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию
type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
 а указать явно, в программе.'''
my_list = ['list', 32, 3.3, True]
for i in my_list:
    print(type(i))
