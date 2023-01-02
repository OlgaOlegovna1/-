# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


my_list = []
for x in range(0, 5):
    my_list.append(randint(1, 10))

print(my_list)
sum_num = my_list[1]+my_list[3]

print(sum_num)