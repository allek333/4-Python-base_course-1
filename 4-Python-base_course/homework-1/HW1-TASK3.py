'''Узнайте у пользователя число n. Найдите сумму чисел
n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

number_str = input('введите целое однозначное число: ')
number_sum_1 = int(number_str)
number_sum_2 = int(number_str + number_str)
number_sum_3 = int(number_str + number_str + number_str)
print(number_sum_1 + number_sum_2 + number_sum_3)
