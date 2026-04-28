# LEN
any_string = 'В середине всего находится Солнце. (Коперник)'
center_index = (len(any_string) - 1) // 2

print('Длина последовательности any_string:', len(any_string))
print('Индекс элемента в середине any_string:', center_index)
print('Значение элемента в середине any_string:', any_string[center_index])





# CONCATENATION
first_vegetable_list = ['помидор', 'огурец', 'баклажан', 'перец']

second_vegetable_list= ['картофель', 'морковь', 'лук', 'чеснок']

full_vegetable_list = first_vegetable_list + second_vegetable_list
print(full_vegetable_list)

# Строки - это последовательности. Объединяем!
hybrid = second_vegetable_list[3] + first_vegetable_list[1]
print(hybrid)





# СРАВНЕНИЕ последовательностей

# При сравнении последовательностей попарно сравниваются элементы
# с одинаковыми индексами:
list_one = [10, 12, 17, 9, 1, 4]
#            |   |   |  |    
list_two = [10, 12, 17, 3, 1, 4]

# Оператор сравнения работает так же, как и при сравнении чисел.
# Выражение с оператором сравнения, как и в случае с числами,
# возвращает True или False.
print(list_one > list_two)

# Сравнение вернуло True, то есть список list_one действительно больше, чем list_two.
# Первые три элемента в этих списках попарно равны, а вот list_one[3] больше, чем list_two[3].
# Различие обнаружено, решение принято, сравнение прекращено: остальные элементы сравниваться не будут.




# ВОПРОС 1
# Какой ответ будет напечатан?
list_one = [8, 15, 17, 9, 11, 2]
list_two = [8, 15, 17, 9, 11, 2]
print(list_one > list_two) 






# ВОПРОС 2
# Какой ответ будет напечатан?
list_one = [3, 1, 16, 9, 10, 4, 15, 3]
list_two = [3, 1, 17, 9, 10, 4]
print(list_one > list_two) 






# ВОПРОС 3
# Какой ответ будет напечатан?
list_one = [1, 2, 3, 4, 5, 6, 7, 8]
list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_one > list_two) 





# ЗАДАНИЕ
Напишите функцию compare_sequences(), которая будет принимать на вход два списка,
сравнивать их — и возвращать сообщение Список <sequence> больше., где <sequence> — это больший из списков.
Для создания сообщения используйте f-строку.
Если списки равны, функция должна вернуть сообщение Списки равны..
Вызовите функцию compare_sequences() и напечатайте результат.
# Пример:
sequence_1 = [15, 22, 18, 19, 21]
sequence_2 = [16, 22, 18, 21]

def compare_sequences(...):
    ...
# печатаем результат. Должно быть напечатано:
# Список [16, 22, 18, 21] больше. 




sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]

def compare_sequences(...):
    ...

# Вызовите функцию compare_sequences(),
# передайте в неё списки sequence_1 и sequence_2.
# Напечатайте результат, который вернёт функция.

print(...)






# РЕШЕНИЕ
sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]

def compare_sequences(one, two):
    if one > two:
        return (f'Список {one} больше.')
    elif one == two:
        return (f'Списки равны.')
    elif one < two:
        return (f'Список {two} больше.')

# Вызовите функцию compare_sequences(),
# передайте в неё списки sequence_1 и sequence_2.
# Напечатайте результат, который вернёт функция.

print(compare_sequences(sequence_1, sequence_2))








# ВОПРОС 4
# Каким будет ответ при сравнении 
# [10, 'one'] > ['one', 10]


# 1. True

# 2. False

# 3. TypeError: '>' not supported between instances of 'int' and 'str'








# ВОПРОС 5
# Что вернёт операция сравнения?
first = [15, 2, '11', 10]
second = [15, 2, '101', 17]

print(first < second)

# 1. True

# 2. False

# 3. TypeError: '>' not supported between instances of 'int' and 'str'