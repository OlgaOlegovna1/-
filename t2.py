# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from random import randint
n = int(input("Введите количество чисел в списке: "))
my_list = []
for x in range(n):
    my_list.append(randint(-10, 10))

print(my_list)


new_list = []
for i in range(n):
    if i!=n:
        new_list.append(my_list[i]*my_list[n-1])  
        n = n-1
    if i==n:
        break
print(new_list)
    

