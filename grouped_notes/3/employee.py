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

from uuid import uuid4

class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        self.employee_id = self.__generate_employee_id()
        self.salary = salary

    def __generate_employee_id(self):
        self._employee_id__ = f'{self.first_name}{self.second_name}{self.gender}'

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
full_time_employee = FullTimeEmployee('Иван', 'Иванов', 'м', 50000)
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

part_time_employee = PartTimeEmployee('Анна', 'Петрова', 'ж')
part_time_employee.consume_vacation(5)
print(part_time_employee.get_vacation_details())
