"""Даны 2 списка:
a = [4,6,'pу','tell',78]
b = [44,'hello',56,'exept',['world',5.7],3,6]

Выполнить следующие операции:
1. Сложить два списка (решить двумя способами).
2. Перенесите 6-ой элемент на 3 позицию уже сложенных списков.
3. Посчитать сколько раз встречается число 6 уже в сложенных списках.
4. Вывести на экран количество элементов сложенного списка.
5. Вывести 1 элемент вложенного списка.
**6. Посчитать сколько раз в общем всречается 1(один) в
следующем списке и его элементах:
[[1,5.1], 1,'hello1world',51,'exept',['orange1',1.7,1],3,6]
В ответе кол-во единиц должно равнятся 8."""

a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', ['world', 5.7], 3, 6]
s_1 = a + b
print(s_1)
# s_2 = [*a, *b]
# print(s_2)

num_m = s_1.pop(5)
s_1.insert(2, num_m)
print(s_1)

count_6 = s_1.count(6)
print(count_6)

len_s = len(s_1)
print(len_s)

print(s_1[9][0])

list_1 = [[1, 5.1], 1, 'hello1world', 51, 'exept', ['orange1', 1.7, 1], 3, 6]
print(list_1)


def unpacking(array: list) -> list_1:
    """
    Recursive algorithm
    with extend/append
      """
    lst = []
    for i in array:
        if isinstance(i, list):
            lst.extend(unpacking(i))
        else:
            lst.append(i)
    return lst


list_simple = unpacking(list_1)
str_simple = "".join(map(str, list_simple))
print(list(str_simple).count("1"))
