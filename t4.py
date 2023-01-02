# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input())
result = []

while a:
    result.append(a % 2)
    a //= 2
result.reverse()
print(*result)