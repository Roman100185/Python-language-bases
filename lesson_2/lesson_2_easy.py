__author__ = 'Roman Puchkov'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# Task_1
print('', '\n')
print('Task_1')
fruits = ["яБлоко", "банАн", "Киви", "аРБуз"]
otstup = ''
num = 1
print('Список фруктов:')
for num, fruit in enumerate(fruits, num):
	print('{}.{:>2}{}'.format(num, otstup, fruit.title()))
print('', '\n')


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


#Task_2
print('Task_2')
spisok1 = [12, 5, 'world', 'sky']
print('Первый список: ', spisok1)
spisok2 = [35, 8, 5, 'pie', 'Ga']
print('Второй список: ', spisok2)
result = set(spisok1) - set(spisok2)
print('Результат исключения дубликатов из первого списка: ', result)
print('', '\n')



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Task_3
print('Task_3')
spisok = [1, 2, 3, 8, 9, 0, 4, 5, 6, 7]
spisok.sort()
a = ''
b = ''
print('Текущий список:', spisok)
print('Количество элементов в списке:', len(spisok))
for i in range(len(spisok)):
	#проверка элементов списка на четность
	if i % 2 == 0:
		a = i/4
		print('Список:', a)
	if i % 2 != 0:
		b = i**2
		print(b)
