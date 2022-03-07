'''Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
затем выведите на экран.'''

data_int = 3
data_float = .3
data_str = ['a, 3']
data_tpl = ('a, 9')
a = ('j')
data_dict = {'a':"d", 2:"3"} # если ключи будут буквами, их надо как-либо определить
print(type(data_int))
print(type(data_float))
print(type(data_str))
print(type(data_tpl))
print(type(data_dict))

data_int = int(input('введите целое число: '))
data_float = float(input('введите десятичную дробь: '))
data_str = str(input('введите слово: '))
data_tpl = tuple(input('введите числовой ряд: '))
name = str(input('введите ваше имя: '))
age = int(input('введите число полных лет: '))
data_dict = {'Вас зовут':str(input('введите ваше имя: ')), 'и на сегодня вам':int(input('введите число полных лет: '))}
print(type(data_int))
print(type(data_float))
print(type(data_str))
print(type(data_tpl))
print(data_dict)
print(type(data_dict))
