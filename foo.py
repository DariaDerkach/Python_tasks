"""1. Сумма цифр

Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать
сумму его цифр."""

# def sum_numb(n):
#     print(sum(int(i) for i in list(n)))
#
#
# sum_numb(input(f"Введите число\n"))

"""
2. Банковский вклад

Пользователь делает вклад в размере а рублей сроком   под 10% годовых 
(каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, 
и на них в следующем году тоже будут проценты).
Написать функцию "bank", принимающая аргументы "а" и "years", и возвращающую сумму, которая 
будет на счету пользователя."""

# def bank(a: int, years: int):
#     vklad = a * ((1.1) ** years)
#     return print(vklad)
#
#
# bank(100, 10)


"""
3. Правильная дата

Написать функцию "date", принимающую 3 аргумента — день, месяц, год. 
Вернуть True, если такая дата есть в нашем календаре, иначе — False.

"""

# def date(day, month, year):
#     month_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,
#                  6: 30, 7: 31, 8: 31, 9: 30, 10: 31,
#                  11: 30, 12: 31
#                  }
#
#     user_date = {month: day}
#     if year in (range(2023)):
#         if year % 4 == 0:
#             month_day[2] = 29
#         if year % 4 == 0 and year % 100 == 0:
#             month_day[2] = 28
#         if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#             month_day[2] = 29
#     if month_day.get(month) >= day and day > 0:
#         print(True)
#     else:
#         print(False)
#
#
# date(30, 2, 1985)

"""
4. Найти всех
Напомним, что строковый метод find(‘a’) возвращает местоположение первого вхождения символа "a" 
в строке. Проблема заключается в том, что данный метод не находит местоположение всех символов "а".

Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: 
строку target и символ symbol и возвращает список, содержащий все местоположения этого 
символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

Примечание 2. Следующий программный код:

print(find_all(‘abcdabcaaa’, ‘a’))
print(find_all(‘abcadbcaaa’, ‘e’))
print(find_all(‘abcadbcaaa’, ‘d’))
должен выводить:

[0, 4, 7, 8, 9]
[]
[4]
"""

# def find_all(target: str, symbol: str) -> list:
#     list_index = []
#     for index, val in enumerate(target):
#         if val == symbol:
#             list_index.append(index)
#         else:
#             continue
#     return list_index
#
#
# print(find_all('abcdabcaaa','a'))
# print(find_all('abcadbcaaa', 'e'))
# print(find_all('abcadbcaaa', 'd'))

"""
5. Ровно в одном
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова 
word1 и word2 и возвращает значение True если слова имеют одинаковую длину и отличаются ровно 
в 1 символе и False в противном случае.

Примечание. Следующий программный код:

print(is_one_away(‘bike’, ‘hike’))
print(is_one_away(‘water’, ‘wafer’))
print(is_one_away(‘abcd’, ‘abpo’))
print(is_one_away(‘abcd’, ‘abcde’))
должен выводить:

True
True
False
False
"""

# def is_one_away(word1: str, word2: str):
#     count = 0
#     for i in word1:
#         for k in word2:
#             if i == k:
#                 count += 1
#
#     if len(word1) == len(word2) and count == len(word1) - 1:
#         return True
#     else:
#         return False
#
#
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))

"""
6. Палиндром 🌶️
 Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и 
 возвращает значение True если указанный текст является палиндромом и False в противном случае.
        
Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
        
Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте 
пробелы, а также символы , . ! ? -.
        
Примечание 3. Следующий программный код:
        
print(is_palindrome(‘А роза упала на лапу Азора.’))
print(is_palindrome(‘Gabler Ruby — burrel bag!’))
print(is_palindrome(‘BEEGEEK’))
должен выводить:
        
        True
        True
        False
"""

# def is_palindrome(word):
#     word_gues = []
#     for i in word:
#         if i == "!" or i == "." or i == "!" or i == "?" or i == "—" or i == "." or i == " ":
#             continue
#         else:
#             word_gues.append(i)
#     result = "".join(word_gues)
#     result = result.lower()
#
#     if result == result[::-1]:
#         return "True"
#     else:
#         return "False"
#
#
# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby — burrel bag!'))
# print(is_palindrome('BEEGEEK'))

"""
7. BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
        
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. 
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
        
    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента 
строковое значение пароля password и возвращает значение True если пароль является действительным 
паролем BEEGEEK банка и False в противном случае.
        
        Примечание. Следующий программный код:
        
print(is_valid_password(‘1221:101:22’))
print(is_valid_password(‘565:30:50’))
print(is_valid_password(‘112:7:9’))
print(is_valid_password(‘1221:101:22:22’))
        
должен выводить:
        
True
False
False
False
"""
# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
#
# def is_valid_password(password):
#     password = [int(i) for i in password.split(':')]
#     f1 = str(password[0])
#     if f1 == f1[::-1] and is_prime(password[1]) and password[2] % 2 == 0 and len(password) == 3:
#         return True
#     else:
#         return False
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))

"""
8. Good password 🌶️
        Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое 
        значение пароля password и возвращает значение True если пароль является надежным и False 
        в противном случае.
        
        Пароль является надежным если:
        
        его длина не менее 8 символов;
        он содержит как минимум одну заглавную букву (верхний регистр);
        он содержит как минимум одну строчную букву (нижний регистр);
        он содержит хотя бы одну цифру.
        Примечание. Следующий программный код:
        
        print(is_password_good(‘aabbCC11OP’))
        print(is_password_good(‘abC1pu’))
        должен выводить:
        
        True
        False
"""

# def is_password_good(password):
#     bb = 0
#     cb = 0
#     dig = 0
#     for i in password:
#
#         if i in 'abcdefghijklmnopqrstuvwxyz':
#             cb += 1
#         elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#             bb += 1
#         elif i in '1234567890':
#             dig += 1
#     if len(password) >= 8 and bb >= 1 and cb >= 1 and dig >= 1:
#         return True
#     else:
#         return False
#
# print(is_password_good('aabbCC11OP'))
# print(is_password_good('abC1pu'))
#

"""       
9. Is a Number Prime? 🌶️
        Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и 
        возвращает значение True если число является простым и False в противном случае.
        
        Примечание. Следующий программный код:
        
        print(is_prime(1))
        print(is_prime(10))
        print(is_prime(17))
        должен выводить:
        
        False
        False
        True
 """

# def is_prime(num):
#     flag = True
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
#
# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(17))


"""
10. Next Prime 🌶️🌶️
        Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное 
        число num и возвращает первое простое число большее числа num.
        
        Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
        
        Примечание 2. Следующий программный код:
        
        print(get_next_prime(6))
        print(get_next_prime(7))
        print(get_next_prime(14))
        должен выводить:
        
        7
        11
        17
"""

# def is_prime(num):
#     flag = True
#
#     for i in range(2, num):
#         if num % i == 0:
#             flag = False
#     if num > 1 and flag == True:
#         return True
#     else:
#         return False
#
#
#
# def get_next_prime(num):
#     num +=1
#     while not is_prime(num):
#         num+=1
#     return num
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))


"""
11. Правильная скобочная последовательность 🌶️
        Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую 
        строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход 
        строка является правильной скобочной последовательностью и False в противном случае.
        
        Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только 
        из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
        
        Примечание 2. Следующий программный код:
        
        print(is_correct_bracket(‘()(()())’))
        print(is_correct_bracket(‘)(())(‘))
        должен выводить:
        
        True
        False """


# def is_correct_bracket(text):
#     otk = 0
#     zak = 0
#
#     for i in text:
#         bal = otk + zak
#         if bal < 0:
#             return False
#         if i == '(':
#             otk += 1
#         if i == ')':
#             zak -= 1
#     bal = otk + zak
#
#     if bal > 0:
#         return False
#     else:
#         return True
#
#
# print(is_correct_bracket('()(()())'))
# print(is_correct_bracket(')(())('))
