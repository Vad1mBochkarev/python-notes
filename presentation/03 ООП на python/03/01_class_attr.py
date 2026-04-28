# После создания объекту доступны все атрибуты — и атрибуты класса, и атрибуты объекта:
class Phone:
    # Атрибут класса.
    line_type = 'проводной'
    
    def __init__(self, dial_type_value):
        # Атрибут объекта.
        self.dial_type = dial_type_value


# Создать объект класса Phone.
rotary_phone = Phone(dial_type_value='дисковый')

# Оба атрибута доступны через объект.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип набора: {rotary_phone.dial_type}')

# Выведется: 
# Тип линии: проводной
# Тип набора: дисковый







# Чтобы поменять значение атрибута объекта, нужно:
1. Создать объект с первоначальным значением атрибута.
2. Через объект обратиться к атрибуту и задать ему новое значение.

class Phone:
    # Атрибут класса.
    line_type = 'проводной'
    
    def __init__(self, dial_type_value):
        # Атрибут объекта.
        self.dial_type = dial_type_value

# Создать объект класса Phone с первоначальным значением 
# атрибута объекта dial_type.
rotary_phone = Phone(dial_type_value='дисковый')

print(f'Тип набора: {rotary_phone.dial_type}')

# Поменять первоначальное значение атрибута объекта dial_type.
rotary_phone.dial_type = 'кнопочный'

print(f'Тип набора: {rotary_phone.dial_type}')

# Выведется: 
# Тип набора: дисковый
# Тип набора: кнопочный






# Значение атрибута класса тоже можно поменять,
# но для его изменения не обязательно создавать объект.
# К атрибуту класса можно обратиться напрямую — через класс:
class Phone:
    # Атрибут класса.
    line_type = 'проводной'
    
    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

# Распечатать значение атрибута класса line_type.
print(f'Тип линии: {Phone.line_type}')
# Поменять значение атрибута класса line_type.
Phone.line_type = 'беспроводной'
# Распечатать новое значение атрибута класса.
print(f'Тип линии: {Phone.line_type}')

# Выведется: 
# Тип линии: проводной
# Тип линии: беспроводной





# Если значение атрибута класса попытаться поменять через объект,
# то в этом случае новое значение получит только этот объект:
class Phone:
    # Атрибут класса.
    line_type = 'проводной'
    
    def __init__(self, dial_type_value):
        # Атрибут объекта.
        self.dial_type = dial_type_value


# Создать объект класса Phone.
rotary_phone = Phone(dial_type_value='дисковый')
keypad_phone = Phone(dial_type_value='кнопочный')

# Распечатать значение атрибута класса.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута line_type для объекта rotary_phone.
rotary_phone.line_type = 'радио'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута класса через класс.
Phone.line_type = 'спутниковый'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Выведется:
# Тип линии: проводной
# Тип линии: проводной
# Тип линии: радио
# Тип линии: проводной
# Тип линии: радио
# Тип линии: спутниковый

# Значение атрибута класса было изменено уже после того, как объект keypad_phone был создан,
# однако объект всё равно «увидел» новое значение.
# Объект не хранит значение атрибута класса, а лишь ссылается на него!!!

# Если же в объекте явно задать новое значение атрибута с именем атрибута класса,
# как это было сделано с объектом rotary_phone, то объект сохранит собственное значение, а не ссылку на класс.












# ЗАДАНИЕ 1
# Расширьте систему учёта отпусков, добавив новые атрибуты в класс Employee:
# атрибут vacation_days со значением по умолчанию 28, который отражает, что у каждого сотрудника по умолчанию есть 28 дней отпуска;
# атрибуты first_name, second_name и gender, которые отвечают за имя, фамилию и пол сотрудника соответственно;
# значения этих атрибутов должны устанавливаться при создании объектов.
# Далее создайте два объекта класса Employee с различными значениями для
# first_name, second_name и gender и выведите на печать информацию о сотрудниках в таком виде:
# Имя: Роберт, Фамилия: Крузо, Пол: м, Отпускных дней в году: 28..
# Для вывода на печать используйте f-строку.


class Employee:
    # Вместо инструкции pass напишите свой код.
    pass

# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(...)
employee2 = Employee(...)

# Допишите код для вывода информации о сотрудниках.
print(...)






# РЕШЕНИЕ
class Employee:
    vacation_days = 28
    
    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
    
    
# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(first_name='Роберт', second_name='Крузо', gender='м')
employee2 = Employee(first_name='Сара', second_name='Коннор', gender='ж')

# Допишите код для вывода информации о сотрудниках.
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, '
      f'Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, '
      f'Пол: {employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.')
