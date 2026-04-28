# ЗАДАНИЕ 1
#На основе заготовленного кода напишите функцию print_friends_count() для вывода количества друзей. При вызове в функцию должно передаваться количество друзей.  Параметр функции должен называться friends_count. 
#Вызовите эту функцию с разными аргументами не менее трёх раз. Функция должна сообщать о количестве друзей при любых целых положительных значениях переменной friends_count.
#Для количества друзей < 20, фраза должна корректно склоняться. Если же друзей очень много — двадцать или больше, — должно выводиться сообщение 'Ого, сколько у тебя друзей! Целых {friends_count}'
# Объявите функцию здес
# Код, написанный ниже, переместите внутрь объявленной вами функции
# if friends_count == 0:
#     print('У тебя нет друзей')
# elif friends_count == 1:
#     print('У тебя', friends_count, 'друг')
# elif friends_count >= 2 and friends_count <= 4:
#     print('У тебя', friends_count, 'друга')
# elif friends_count >= 5 and friends_count < 20:
#     print('У тебя', friends_count, 'друзей')
# else:
#     print('Ого, сколько у тебя друзей! Целых', friends_count)
# Напишите вызов функции

def print_friends_count(friends_count):
    if friends_count == 0:
        print('У тебя нет друзей')
    elif friends_count == 1:
        print('У тебя', friends_count, 'друг')
    elif friends_count >= 2 and friends_count <= 4:
        print('У тебя', friends_count, 'друга')
    elif friends_count >= 5 and friends_count < 20:
        print('У тебя', friends_count, 'друзей')
    else:
        print('Ого, сколько у тебя друзей! Целых', friends_count)

print_friends_count(0)
print_friends_count(1)
print_friends_count(3)
print_friends_count(13)
print_friends_count(35)