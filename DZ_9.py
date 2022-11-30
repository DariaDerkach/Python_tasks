"""1. Ввести в файл 'input.txt' 2 числа в одну строку через пробел.
Вывести в файл 'output.txt' их разность."""

file_1 = open("input.txt", 'w')
file_1.write('4 8')
file_1.close()

file_1 = open("input.txt", 'r')
a = file_1.readline().split(" ")
file_1.close()
raz = str(int(a[0]) - int(a[1]))

out = open("output.txt", 'w')
out.write(raz)
out.close()

"""2. Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых 
файла: test_1.txt, test_2.txt, test_3.txt.
Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt
После этого удалите созданную папку.
Все операции выполнять с помощью встроенных функций библиотеки os."""

import os

os.chdir('..\..')
os.chdir('Desktop')
print(os.getcwd())
if not os.path.isdir('txt'):
    os.mkdir('txt')
os.chdir('txt')

text_file_1 = open("test_1.txt", "w")
text_file_1.close()
os.rename('test_1.txt', 'rename_1.txt')
os.remove("rename_1.txt")
text_file_2 = open("test_2.txt", "w")
text_file_2.close()
os.rename('test_2.txt', 'rename_2.txt')
os.remove("rename_2.txt")
text_file_3 = open("test_3.txt", "w")
text_file_3.close()
os.rename('test_3.txt', 'rename_3.txt')
os.remove("rename_3.txt")
os.chdir('..')
os.rmdir('txt')
print(os.getcwd())

"""
3. В текстовом файле посчитать количество строк, а также для каждой 
отдельной строки определить количество в ней символов. 
Помним, что '\n' не должны учитываться как отдельные строки."""

with open("C:/Users/1/PycharmProjects/pythonProject1/text_file.txt", encoding='utf-8') as f:
    for line in f:
        print(len(line.strip()), 'символов.')

print(sum(1 for line in open("C:/Users/1/PycharmProjects/pythonProject1/text_file.txt", "r")))
