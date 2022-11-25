""" 1. Создайте кортеж с одним элементом

2. Создайте кортеж из 10 случайно сгенирированных чисел
от -100 до 100.
Найдите индексы максимального и минимального элемента.
Решить 3-мя способами.

3. Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму.
Решить 2-мя способами(через цикл и через встроенную функцию сложения)

4. Выведите статистику частности букв в кортеже
long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
 'и', 'и', 'т', 'т', 'а', 'и', 'и',
 'и', 'и', 'и', 'т', 'и')
Например: 'Буква "и" встречается 11 раз' (и так с каждой)
Решить 2-мя способами через цикл и через метод."""

import random

# 1
a = (5,)
print(type(a))

# 2.1
n = 0
tuple_random = []
while n <= 9:
    b = random.randint(-100, 100)
    n = n + 1
    tuple_random.append(b)
x = tuple(tuple_random)
print(x)
print(x.index(max(x)))
print(x.index(min(x)))

# 2.2
x_1 = [random.randint(-100, 100) for i in range(10)]
x_1 = tuple(x_1)

max_x_1 = x_1[0]
min_x_1 = x_1[0]
for i in x_1:
    if i <= max_x_1:
        min_x_1 = i
    if i >= max_x_1:
        max_x_1 = i
print(x_1)
print(max_x_1)
print(min_x_1)

# 2.3
x_2 = sorted([random.randint(-100, 100) for i in range(10)])
x_2 = tuple(x_2)
print(x_2)
print(x_2[0])
print(x_2[-1])

# 3.1
x_3 = [i for i in range(10)]
x_3 = tuple(x_3)
print(x_3)
print(sum(x_3))

# 3.2
sum_x_3 = 0
for i in x_3:
    sum_x_3 = sum_x_3 + i
print(sum_x_3)

# 4
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и',
             'и', 'и', 'т', 'т', 'а', 'и', 'и',
             'и', 'и', 'и', 'т', 'и')
print(long_word.count('т'))
print(long_word.count('а'))
print(long_word.count('и'))

sum_t = 0
sum_a = 0
sum_i = 0
for i in long_word:
    if i == "т":
        sum_t = sum_t + 1
    if i == "а":
        sum_a += 1
    if i == "и":
        sum_i += 1
print(sum_i)
print(sum_a)
print(sum_t)
