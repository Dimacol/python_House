# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

day = int(input('Введите порядковый номер дня недели: '))
if day > 7 or day < 1:
    print('Повторите правильный ввод от 1 до 7')
elif day == 6 or day == 7:
    print("да")
else:
    print("нет")
