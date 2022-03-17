# TASK1
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

# TASK2
'''Пользователь вводит время в секундах. Переведите время в часы, минуты,
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.'''

number_base = int(input('введите целое число: '))
number_hours = int(number_base // 3600)
number_minutes = int(number_base % 60 / 6)
number_seconds = int(number_base % 60 % 6 * 10)
result = f'in format {number_hours:02}:{number_minutes:02}:{number_seconds:02}'
# в f-строках количество разрядов работает только с integer
print(number_hours)
print(number_minutes)
print(number_seconds)
print(result)

# TASK3
'''Узнайте у пользователя число n. Найдите сумму чисел
n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

number_str = input('введите целое однозначное число: ')
number_sum_1 = int(number_str)
number_sum_2 = int(number_str + number_str)
number_sum_3 = int(number_str + number_str + number_str)
print(number_sum_1 + number_sum_2 + number_sum_3)

# TASK4
'''Пользователь вводит целое положительное число. Найдите самую большую
цифру в числе. Для решения используйте цикл while и арифметические операции.'''

number = int(input('введите целое число: '))
while True:
    number_1 = number / 10
    number_2 = number % 10
    number_1 < number_2 # сравнение цифр по разрядам. Очевидно что заданное число
    #будет уменьшено до единичного разряда. После происходит сравнение со следующей
    #цифрой. Цикл будет продолжаться, пока не закончится перебор всего числа.
    print(number_2)
    break

# TASK5
'''Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким
финансовым результатом работает фирма. Например, прибыль — выручка больше издержек,
или убыток — издержки больше выручки. Выведите соответствующее сообщение.

Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение
прибыли к выручке. Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчёте на одного сотрудника.'''

# через цикл while так и не смог заставить корректно работать, получилось
# только через if
profit = int(input('введите прибыль фирмы: '))
costs = int(input('введите издержки фирмы: '))
while profit > costs:
    print('фирма работает с доходом: ', profit - costs)
    print('рентабельность выручки равна: ', (profit - costs) / profit * 100, '%')
    staff = int(input('введите количество сотрудников: '))
    print('доход на одного сотрудника равен: ', (profit - costs) / staff)
    # break
    if profit < costs:
        continue
    print('фирма работает с убытком: ', costs - profit)
    break

profit = int(input('введите прибыль фирмы: '))
costs = int(input('введите издержки фирмы: '))
while True:
    if profit > costs:
        print('фирма работает с доходом: ', profit - costs)
        print('рентабельность выручки равна: ', (profit - costs) / profit * 100, '%')

    # continue
    if profit < costs:
        continue
    print('фирма работает с убытком: ', costs - profit)
# !!!не печатае принт при работе фирмы в убыток
profit = int(input('введите прибыль фирмы: '))
costs = int(input('введите издержки фирмы: '))
if profit > costs:
    print('фирма работает с доходом: ', profit - costs)
    print('рентабельность выручки равна: ', (profit - costs) / profit * 100, '%')
    staff = int(input('введите количество сотрудников: '))
    print('доход на одного сотрудника равен: ', (profit - costs) / staff)
elif profit < costs:
        # continue
    print('фирма работает с убытком: ', costs - profit)


# TASK6
'''Спортсмен занимается ежедневными пробежками. В первый день
его результат составил a километров. Каждый день спортсмен увеличивал
результат на 10% относительно предыдущего. Требуется определить номер
дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно
натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.'''


a = int(input('input real number - initial: '))
b = int(input('input real number - target: '))
n = 1
while a < b:
    print(n, '- th day: ', a)
    a = a + a * 0.1
    n = n + 1
else:
    print('on the', n, '- th day the athlete take a goal: not less', b, 'km')
