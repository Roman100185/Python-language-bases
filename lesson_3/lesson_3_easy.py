__author__ = 'Roman Puchkov'


# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = str(number)
    # для начала разделим символы до и после точки
    a = number.split('.')[1]
    b = number.split('.')[0]
    # сделаем срез по какому символу будем проверять на округление и преобразуем в int
    c = int(a[ndigits-1:ndigits])
    d = int(a[0:ndigits])
    # условие округления
    if c >= 6:
        e = d + 1
    else:
        e = d
    # проверяем длину строки чтоб определить степень округления
    if len(str(d)) == len(str(e)):
        res = [b + '.' + str(e)]
    if len(str(d)) < len(str(e)):
        res = [int(b) + 1]
    # преобразуем склеенные строки в float
    result = list(map(float, res))
    return result

print('\n', 'Task 1', '\n')
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print('-' * 200)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    a2 = int(ticket_number[:1]) + int(ticket_number[1:2]) + int(ticket_number[2:3])
    b2 = int(ticket_number[3:4]) + int(ticket_number[4:5]) + int(ticket_number[-1:])
    if a2 == b2:
        return 'Lucky ticket'
    else:
        return 'You lose...'

print('\n', 'Task 2', '\n')
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))