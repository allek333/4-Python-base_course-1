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
