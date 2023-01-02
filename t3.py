# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным и 
#  минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from random import randint

N = 7
list_of_nums = []

index_of_min, index_of_max = 0, 0

for index in range(N):
    rand_num = randint(1, 900) / 100*2
    list_of_nums.append(rand_num)
    if rand_num < list_of_nums[index_of_min]:
        index_of_min = index
    if rand_num > list_of_nums[index_of_max]:
        index_of_max = index

print(list_of_nums)