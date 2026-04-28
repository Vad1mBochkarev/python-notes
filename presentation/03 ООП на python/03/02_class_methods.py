class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    # Это новый метод, уже с двумя параметрами.
    def call(self, phone_number):
        # Сначала в вывод подставляется значение параметра phone_number,
        # а затем - атрибута класса Phone.
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


rotary_phone = Phone(dial_type_value='дисковый')

# Вызов метода call(). Передаётся аргумент '555-2368'
# для параметра phone_number.
rotary_phone.call('555-2368')

# Выведется:
# Звоню по номеру 555-2368! Тип связи - проводной.



# В методе call не только используется переданный аргумент phone_number,
# но есть и обращение к атрибуту line_type: через этот атрибут уточняется тип линии для конкретного телефона.
# При создании объекта атрибут класса становится атрибутом конкретного объекта,
# и это значит, что обращаться к этому атрибуту нужно через self.






# Можно создать сколько угодно методов в классе, и все они могут влиять на поведение объекта.
# Например, вы можете наделить телефоны возможностью оповещать вас о количестве пропущенных вызовов:
class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    # Ещё один метод.
    def get_missed_calls(self):
        print('Запрос количества пропущенных вызовов.')


rotary_phone = Phone(dial_type_value='дисковый')

rotary_phone.get_missed_calls()

# Выведется:
# Запрос количества пропущенных вызовов.






# Замена значений атрибутов через метод
# Значения атрибутов можно поменять через точечную нотацию: 
class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value


# Вот тут задано первоначальное значение.
rotary_phone = Phone(dial_type_value='дисковый')

print(rotary_phone.dial_type)

# А тут - новое.
rotary_phone.dial_type = 'кнопочный'

print(rotary_phone.dial_type)

# Выведется:
# дисковый
# кнопочный



# Также для этой задачи можно использовать метод. 
class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    # Новый метод.
    def dial_type_upgrade(self, new_dial_type):
        # Задать для атрибута dial_type новое значение - new_dial_type.
        self.dial_type = new_dial_type


# Тут задано начальное значение атрибута dial_type.
rotary_phone = Phone(dial_type_value='дисковый')

print(rotary_phone.dial_type)

# Вызов метода dial_type_upgrade, который призван поменять
# начальное значение атрибута на new_dial_type.
rotary_phone.dial_type_upgrade('кнопочный')

print(rotary_phone.dial_type)

# Выведется:
# дисковый
# кнопочный





# ЗАДАНИЕ 2
# Добавьте в вашу систему учёта отпусков возможность узнавать, сколько дней отпуска осталось у того или иного сотрудника. 
# Для этого дополните класс Employee следующими методами:
# Метод consume_vacation должен отвечать за списание дней отпуска.

# Единственный параметр этого метода (кроме self) — количество потраченных отпускных дней (целое число).

# При вызове метода consume_vacation соответствующее количество дней должно вычитаться из общего числа
# доступных отпускных дней сотрудника.

# Чтобы определить число доступных отпускных дней конкретного сотрудника,
# в классе опишите атрибут экземпляра remaining_vacation_days,
# который по умолчанию будет равен значению атрибута класса vacation_days, и используйте этот атрибут в работе метода.
# Метод get_vacation_details должен возвращать остаток отпускных дней сотрудника в формате: Остаток отпускных дней:
#       <число>..

# Чтобы проверить работу программы:
# 1. Создайте экземпляр класса Employee.
# 2. Вызовите метод consume_vacation, указав подходящее значение аргумента, например 7.
# 3. Вызовите метод get_vacation_details.


class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        # Сюда добавьте новый атрибут remaining_vacation_days

    # Сюда добавьте методы consume_vacation и get_vacation_details.

# Пример использования класса, раскомментируйте, когда задание будет готово:
# employee = Employee('Роберт', 'Крузо', 'м')
# employee.consume_vacation(7)
# print(employee.get_vacation_details())




# ПОДСКАЗКИ
# Чтобы определить методы экземпляра, используйте обычный синтаксис функций, но не забудьте добавить self в качестве первого аргумента.
# Чтобы изменить атрибут экземпляра в методе, используйте self.<имя атрибута>.
# Чтобы вернуть информацию из метода, используйте return.
# Атрибут экземпляра со значением по умолчанию можно задать так: self.remaining_vacation_days = Employee.vacation_days.


# РЕШЕНИЕ
class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
    

employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())







# __STR__
class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    def dial_type_upgrade(self, new_dial_type):
        self.dial_type = new_dial_type


rotary_phone = Phone(dial_type_value='дисковый')

print(rotary_phone)
# <__main__.Phone object at 0x7f323b5f8310>






class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    def dial_type_upgrade(self, new_dial_type):
        self.dial_type = new_dial_type

    # Вот он - магический метод __str__ с пользовательским описанием!!!
    def __str__(self):
        return f'Это {self.line_type} телефон. Набор - {self.dial_type}.'


rotary_phone = Phone(dial_type_value='дисковый')

print(rotary_phone)
