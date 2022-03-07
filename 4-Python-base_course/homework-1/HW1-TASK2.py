'''Пользователь вводит время в секундах. Переведите время в часы, минуты,
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

number_base = int(input('введите целое число: '))
number_hours = int(number_base // 3600)
number_minutes = int(number_base % 60 / 6)
number_seconds = int(number_base % 60 % 6 * 10)
result = f'in format {number_hours:02}:{number_minutes:02}:{number_seconds:02}'#
# в f-строках количество разрядов работает только с integer
print(number_hours)
print(number_minutes)
print(number_seconds)
print(result)
