# Родительский класс.
class Phone:

    # Атрибут базового класса.
    line_type = 'проводной'

    # Инициализатор базового класса.
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    # Метод базового класса.
    def ring(self):
        print('Дзззззыыыыыыыынь!')

    # Ещё один метод базового класса.
    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


# Дочерний класс, унаследованный от класса Phone.
class MobilePhone(Phone):
    pass 

# В теле нового класса нет кода, но он вполне рабочий,
# потому что наследует все методы и атрибуты родительского класса Phone!



# Например, вы можете создать объект класса MobilePhone, задать ему свой тип набора и попросить его прозвенеть:
class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    pass


mobile_phone = MobilePhone('сенсорный')

mobile_phone.ring()

# Выведется:
# Дзззззыыыыыыыынь!





# Пусть в классе MobilePhone значение атрибута line_type будет беспроводной.
# И пусть мобильный телефон звонит иначе: не 'Дзззззыыыыыыыынь!', а 'Дзынь-Дзынь!'.
class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    # Переопределить значение атрибута line_type класса Phone.
    line_type = 'беспроводной'

    # Переопределить метод ring() класса Phone.
    def ring(self):
        print('Дзынь-дзынь!')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный')

# Распечатать значение атрибута line_type для объекта класса Phone.
print(rotary_phone.line_type)
# Вызвать метод ring() для объекта класса Phone.
rotary_phone.ring()

# Распечатать значение атрибута line_type для объекта класса MobilePhone.
print(mobile_phone.line_type)
# Вызвать метод ring() для объекта класса MobilePhone.
mobile_phone.ring()

# Вывод:
# проводной
# Дзззззыыыыыыыынь!
# беспроводной
# Дзынь-дзынь!




# Новые атрибуты для дочерних классов
class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    # Инициализатор класса MobilePhone с новым параметром - network_type.
    def __init__(self, dial_type_value, network_type):
        # Новый атрибут объекта.
        self.network_type = network_type
        # Вызов родительского инициализатора.
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')



# И новый метод
class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')



class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    # Новый метод.
    def start_game(self):
        print('Игра запущена!')


mobile_phone = MobilePhone('сенсорный', 'LTE')

print(mobile_phone.battery_type)
print(mobile_phone.network_type)
mobile_phone.start_game()

# Вывод:
# Li-ion
# LTE
# Игра запущена!







# У объектов дочерних классов есть доступ к атрибутам и методам родительского класса,
# а вот объекты родительского класса не могут воспользоваться возможностями дочернего. 
...

rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный', 'LTE')

print(mobile_phone.battery_type)
print(mobile_phone.network_type)
mobile_phone.start_game()

# Выведется:
# Li-ion
# LTE
# Игра запущена!

# Объект родительского класса Phone обращается к атрибуту дочернего класса
# MobilePhone.
print(rotary_phone.battery_type)

# Выведется:
# AttributeError: 'Phone' object has no attribute 'battery_type'
# Ошибка атрибута: у объектов класса 'Phone' нет атрибута 'battery_type'




# ЗАДАНИЕ: Наследование
# В ОднойБольшойИзвестнойКомпании, для которой вы разрабатываете систему учёта отпусков,
# есть сотрудники с полной и частичной занятостью — фултаймеры и парт-таймеры.

# И фултаймеры, и парт-таймеры могут взять оплачиваемый отпуск:
# - оплачиваемый отпуск у фултаймера — 28 дней,
# - оплачиваемый отпуск у парт-таймера — 14 дней.

# Фултаймеры, кроме оплачиваемого отпуска, могут взять также неоплачиваемый. 
# Напишите программу, которая управляет данными о сотрудниках и их отпусках.

# Что нужно сделать:
# 1. Опишите классы FullTimeEmployee и PartTimeEmployee, они должны наследоваться от Employee.
# Экземпляры этих классов должны хранить данные о сотрудниках (имя, пол и доступное для сотрудника количество дней отпуска).

# 2. В класс FullTimeEmployee добавьте метод get_unpaid_vacation(). Этот метод должен
# принимать два параметра: 
# -дату начала неоплачиваемого отпуска (строка), 
# -необходимое количество дней (целое число);
# возвращать сообщение в формате: 'Начало неоплачиваемого отпуска: <дата>, продолжительность: <число> дней.'.

# 3. В классе PartTimeEmployee переопределите атрибут vacation_days. Его значение по умолчанию должно быть 14.


# В конце прекода описаны экземпляры обоих классов.
# При желании перед отправкой кода на проверку запустите код и проверьте работу новых методов и атрибутов.
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

# Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee.

# Пример использования:
# full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
# part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
# print(part_time_employee.get_vacation_details())


# ПОДСКАЗКИ
# Для наследования используйте такой синтаксис: class ClassName(ParentClass):.
# Чтобы переопределить атрибут класса vacation_days — в классе PartTimeEmployee создайте атрибут класса с новым значением: 14.
# Чтобы переопределить атрибут объекта remaining_vacation_days
# объявите инициализатор класса __init__(...),
# вызовите в нём инициализатор родительского класса: super().__init__(...),
# после этого переопределите значение атрибута: self.remaining_vacation_days = PartTimeEmployee.vacation_days.





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


class FullTimeEmployee(Employee):
    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
    
    def get_unpaid_vacation(self, start_date, days_unpaid):
        return (f'Начало неоплачиваемого отпуска: {start_date}, ' 
                f'продолжительность: {days_unpaid} дней.')
    
class PartTimeEmployee(Employee):   
    vacation_days = 14
    
    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days
    
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())






# Полиморфизм
# Метод один и тот же, но в каждом классе он работает по-разному. 
class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    def start_game(self):
        print('Игра запущена!')

    # Здесь переопределён метод __str__ .
    def __str__(self):
        return f'У мобильного телефона {self.dial_type} тип набора номера'


# Создать объект mobile_phone класса MobilePhone
mobile_phone = MobilePhone('сенсорный', 'LTE')

# Распечатать объект mobile_phone.
print(mobile_phone)
print(MobilePhone.line_type)

print(Phone)






# Инкапсуляция
# Защищённые атрибуты и методы
class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value
        # Вот он - защищённый атрибут. Значением будет
        # ID ячейки памяти аргумента dial_type_value.
        self._serial_number = id(dial_type_value)

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.__network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    # Это публичный метод, в котором используется защищённый атрибут.
    # Метод определён в классе-наследнике, защищённые атрибуты можно
    # использовать напрямую в базовом классе и его наследниках.
    def get_info(self):
        print(f'Серийный №: {self._serial_number}, тип: {self.__network_type}')




# ЗАДАНИЕ: инкапсуляция, приватные и защищенные методы и атрибуты
# В классы Employee и FullTimeEmployee добавьте защищённые и приватные атрибуты и методы, решив следующие задачи:
# 1. У каждого сотрудника, независимо от его роли, в системе учёта отпусков должен быть свой идентификатор.
# Использование базового класса для определения общих атрибутов позволяет подклассам наследовать эти атрибуты.

# Доступ к идентификатору ограничивать не надо, но намекнуть другим разработчикам на то,
# что атрибут предназначен для внутреннего использования в классе и его наследниках, стоит.

# В класс Employee добавьте защищённый атрибут _employee_id,
# значение которого должно генерироваться автоматически при создании любого объекта класса или его наследника.

# Генерация идентификатора должна осуществляться в приватном методе __generate_employee_id.
# Идентификатором сотрудника должен быть результат работы встроенной функции hash() из строки,
# полученной в результате конкатенации имени, фамилии и пола.

# 2. Работникам на полной ставке положены отпускные выплаты.
# Они рассчитываются на основании зарплаты, а информация о зарплате не должна быть
# доступна всем желающим или случайно изменена.

# В класс FullTimeEmployee добавьте приватный атрибут __salary,
# значение которого берётся из аргумента, переданного при создании объекта класса,
# и приватный метод __get_vacation_salary, который возвращает значение отпускных из расчёта 80% от суммы заработной платы.


# Создайте экземпляры классов FullTimeEmployee и PartTimeEmployee,
# используйте их методы и проверьте корректность работы защищённых и приватных элементов.

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


class FullTimeEmployee(Employee):

    def get_unpaid_vacation(self, start_date, days):
        return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'

class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


# Пример использования:
# full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

# part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
# part_time_employee.consume_vacation(5)
# print(part_time_employee.get_vacation_details())




# ПОДСКАЗКИ
# Для описания дополнительного атрибута объекта:
# сначала в инициализаторе дочернего класса вызовите инициализатор родительского класса: super().init(...),
# затем определите дополнительный атрибут дочернего класса.
# Для генерации идентификаторов используйте следующий синтаксис: hash(self.first_name + self.second_name + self.gender).




# РЕШЕНИЕ
class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        self._employee_id = self.__generate_employee_id()
        
    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
    
    def __generate_employee_id(self):
        return hash(self.first_name + self.second_name + self.gender)


class FullTimeEmployee(Employee):
    def __init__(self, first_name, second_name, gender, __salary):
        self.__salary = float(__salary)
        
    def __get_vacation_salary(self):
        salary80 = self.__salary / 100 * 80
        return salary80

    def get_unpaid_vacation(self, start_date, days):
        return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {days} дней.'
                              

class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)
        self.remaining_vacation_days = PartTimeEmployee.vacation_days


# Пример использования:
full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
print(full_time_employee._FullTimeEmployee__salary)

part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())
