'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
 деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления
 на ноль.'''

def my_num(a, b):
    try:
        answer = a/b
        return answer
    except ZeroDivisionError:
        return 'b cannot be zero'
print(my_num(float(input('enter num1: ')), float(input('enter num2: '))))
