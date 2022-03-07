''  Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Осуществить вывод данных
о пользователе одной строкой.'''

def my_func():
    first_name = str(input("назовите себя: "))
    second_name = str(input("и фамилию тоже: "))
    year_of_birth = int(input("введите год рождения: "))
    sity = str(input("в каком городе живёте: "))
    email = str(input("ваше мыло: "))
    phone = int(input("ваш телеофон: "))
    return first_name, second_name, year_of_birth, sity, email, phone


first_name_, second_name_, year_of_birth_, sity_, email_, phone_ = my_func()
print(f'вас зовут - {first_name_} с фамилией - {second_name_} года рождения {year_of_birth_} из города {sity_}, с емейлом {email_} и телефоном {phone_}')
