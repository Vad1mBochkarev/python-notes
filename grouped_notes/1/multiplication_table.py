# Задача дописать код, чтобы получилась таблица умножения
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(number_1, '*', number_2, '=', number_1 * number_2)

for num in numbers:
    number_1 = num
    for num2 in numbers:
        number_2 = num2
        print(number_1, '*', number_2, '=', number_1 * number_2)
