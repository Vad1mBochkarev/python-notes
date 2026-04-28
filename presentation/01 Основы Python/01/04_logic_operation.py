beaufort = 0

# Если ветер шесть баллов или больше
if beaufort >= 6:
    print('Будьте осторожны, сильный ветер!')

# Если ветер в четыре балла или менее
if beaufort <= 4:
    print('Лёгкий ветер')

# Если есть хоть какой-то ветер 
if beaufort != 0:
    print('Ветрено') 



# если ветер от 9 до 11 баллов, то это шторм (различной силы)
if beaufort == 0:
    print('Штиль')
elif beaufort == 1:
    print('Тихий ветер')
elif beaufort == 2:
    print('Лёгкий ветер')
elif beaufort == 3:
    print('Слабый ветер')
elif beaufort == 4:
    print('Умеренный ветер')
elif beaufort == 5:
    print('Свежий ветер')
elif beaufort == 6:
    print('Сильный')
elif beaufort == 7 or beaufort == 8:
    print('Крепкий ветер')
elif beaufort >= 9 and beaufort <= 11:
    print('Шторм')
elif beaufort == 12:
    print('Ураган')
else:  # else тоже может быть в конце, после цепочки elif
    print('Неизвестное значение') 






for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    
    if current_hour >= 6 and current_hour <= 11 :  
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:  
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:                       
        print('Добрый вечер!')
    elif current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')




for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас', messages_count, 'новое сообщение')
    elif messages_count >= 2 and messages_count <= 4:
        print('У вас', messages_count, 'новых сообщения')
    else:
        print('У вас', messages_count, 'новых сообщений')




# СОСТАВНЫЕ ЛОГИЧЕСКИЕ ВЫРАЖЕНИЯ
print(True)
# Без неожиданностей, будет напечатано: True

print(not True)
# Будет напечатано: False

print(not False)
# Будет напечатано: True 



print(5 > 3) 
# Будет напечатано: True

print(not 5 > 3)
# Будет напечатано: False 



wind = True

# Есть ли ветер?
if not wind: # Если wind НЕ равен True
    print('Ночь тиха')
else:
    print('Поднялся ветер')
    print('Серые тучи развеял')
    print('Новые тянутся с юга')




# ЗАДАНИЕ 
# Что будет напечатано, если выполнить этот код?
x = 44

if not x > 40 or x < 45 and x != 42:
    print("Выражение вернуло True!")
else:
    print("Выражение вернуло False!") 

# Ответы:
# 1. "Выражение вернуло True!"
# 2. "Выражение вернуло False!"







# Продуктов маловато:
milk = not True       # Молоко "НЕ есть".
cereals =  True        # Хлопья есть.
eggs = False          # Яиц нет.


if milk and cereals or eggs:
    if eggs:
        if milk:
            breakfast = "- омлет"
        else:
            breakfast = "- яичница"
    else:
        breakfast = "- хлопья с молоком"
else:
    if milk:
        breakfast = "- стакан молока"
    elif cereals:
        breakfast = "можно погрызть сухих хлопьев"
    else:
        breakfast = "ничего не будет: разгрузочный день"

print("Сегодня на завтрак", breakfast)
