__author__ = 'Roman Sergeevich Puchkov'



#Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Task_1

num=int(input("Enter number from 1 to 10 "))
while num<=10:
	num+=2
	print(num)

	
	
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# Task_2.1

num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num1,num2=num2,num1 #поменять местами переменные
print("First number is", num1)
print("Second number is", num2)

# Task_2.2

num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
num1=num1+num2 #поменять местами переменные при помощи арифметических операций
num2=num1-num2
num1=num1-num2
print("First number is", num1)
print("Second number is", num2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Task_3

name=input("Enter your name ")
age=int(input("Enter your age "))
if age >= 18:
	print (name,", you can enter!")
	access = True
else:
	print (name,", sorry, but you have to leave this resource!")
	access = False
