__author__ = 'Roman Sergeevich Puchkov'



# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Task_1
	
number=list(input("Enter number: ")) #преобразование числа в список
print(number)
min(number)
print("Min number is:",min(number))
max(number)
print("Max number is:",max(number))



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# Task_2.1 - сделал по аналогии с easy

num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num1,num2=num2,num1 #поменять местами переменные
print("First number is", num1)
print("Second number is", num2)

# Task_2.2 - сделал по аналогии с easy

num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num1=num1+num2 #поменять местами переменные при помощи арифметических операций
num2=num1-num2
num1=num1-num2
print("First number is", num1)
print("Second number is", num2)



# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# Task_3

import math

answer = ''#пустая переменная
while answer !='N': #цикл для работы по запросу, пока пользователь не введет "N"
	answer = input("Поработаем? (Y/N)")
	if answer == 'Y':
		print("Приступим!")
		a=float(input("Enter 'a':"))
		b=float(input("Enter 'b':"))
		c=float(input("Enter 'c':"))
		D=b**2-4*a*c
		print("D=b**2-4*a*c=",D)
		if D==0:
			print("Уравнение имеет 1 корень:")
			x=-b/(2*a)
			print("x=", x)
		elif D>0:
			print("Уравнение имеет 2 различных вещественных корня:")
			x1=(-b + math.sqrt(D)) / (2 * a)
			print("x1=", x1)
			x2=(-b - math.sqrt(D)) / (2 * a)
			print("x2=", x2)
		else:
			print("Уравнение не имеет вещественных корней.")
	elif answer == 'N':
		print("Досвидания!")
	else:
		print("Что это? Я не понимаю!")
