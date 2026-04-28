around_zero = range(-3, 3)

# Вместо списка в цикл передаётся переменная around_zero, 
# в ней хранится range() от -3 до 3
for i in around_zero:
    # Перебрать все числа в диапазоне от -3 до 3 и напечатать их:
    print(i)
# Будет напечатано
# -3
# -2
# -1
# 0
# 1
# 2 



# Цикл переберёт все числа в диапазоне от -3 до 3 и напечатает их:
for i in range(-3, 3):
    print(i)

# Результат будет тот же 








# Функция range() не включает в последовательность чисел второй аргумент,
# поэтому для reversed(range(1, 13)) отсчёт начнётся с 12.
for i in reversed(range(1, 13)):
    print(i, 'бомм!')

print('C новым годом!')





countdown_str = ''

for x in reversed(range(11)):
    countdown_str = countdown_str + str(x) + ", "

countdown_str = countdown_str + 'поехали!'

print(countdown_str)
