# ЗАДАНИЕ 1: декораторы
# Напишите декоратор format_float_return().
# Этот декоратор должен проверять значение, которое возвращает задекорированная функция,
# и если возвращается значение типа float, то декоратор должен округлить это значение до двух знаков после точки.
# Если задекорированная функция возвращает любой другой тип данных, декоратор не должен изменять возвращаемый результат.
# Для округления примените функцию round(). Описание этой функции есть в документации.


from random import choice, uniform


def format_float_return(...):
    # Ваш код здесь


# Не изменяйте код ниже: он поможет проверить работу декоратора.
# Декорируем функцию:
@format_float_return
def test_function_1():
    """Возвращает случайное число типа float в диапазоне от -10 до 10,
    например -4.3897268052813265.
    """
    return uniform(-10, 10)


# Декорируем вторую функцию:
@format_float_return
def test_function_2():
    """Возвращает случайный элемент списка sequence - число или строку."""
    sequence = [
        3.1415926535,
        'pi',
        3.14,
        'пи',
        'три целых четырнадцать сотых',
        3.14159
    ]
    # Функция choice() из модуля random возвращает 
    # случайный элемент последовательности.
    return choice(sequence)


# Вызовем задекорированные функции для проверки работы декоратора:
print(test_function_1())
print(test_function_2())



# ПОДСКАЗКИ
# 1. Используйте isinstance() для проверки типа возвращаемого значения.
# 2. Функция round() поможет вам округлить число.
# 3. Декоратор должен принимать функцию и возвращать функцию.




# РЕШЕНИЕ





# ДЕКОРАТОРЫ для методов классов
class Robot:
    # Состояние батареи базовой станции:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    def update_base_battery_status(self, new_status):
        """Обновляет состояние батареи базовой станции."""
        self.base_battery_status = new_status

    def report(self):
        """Печатает в консоли состояние батареи базовой станции."""
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )


# Создаём двух роботов:
robot1 = Robot('R2-D2')
robot2 = Robot('C-3PO')

# Печатаем состояние батареи:
robot1.report()
robot2.report()

# Обновляем статус батареи - но только в одном из роботов:
robot1.update_base_battery_status(80)

# Снова печатаем состояние батареи:
robot1.report()
robot2.report() 
# Видим, что изначально все методы принадлежат экземплярам




# Теперь сделали метод класса с помощью декоратора
# Методы класса
class Robot:
    # Состояние батареи базовой станции:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    # Декорируем и изменяем метод update_base_battery_status(),
    # чтобы менять значение атрибута не в объекте, а в классе:
    @classmethod
    def update_base_battery_status(cls, new_status):  # Указываем аргумент cls.
        """Обновляет состояние батареи базовой станции."""
        # Присваиваем новое значение атрибуту класса.
        cls.base_battery_status = new_status

    def report(self):
        """Печатает в консоли состояние батареи базовой станции."""
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )


# Создаём двух роботов:
robot1 = Robot('R2-D2')
robot2 = Robot('C-3PO')

# Печатаем состояние батареи:
robot1.report()
robot2.report()

# Обновляем статус батареи в классе: обращаемся не к объекту, а к классу.
Robot.update_base_battery_status(80)

# Снова печатаем состояние батареи:
robot1.report()
robot2.report() 
# Значение атрибута base_battery_status хранится на уровне класса.
# Метод update_base_battery_status() изменяет это значение в классе, а не в объекте. 

# Метод update_base_battery_status() доступен для любого объекта класса Robot,
# таким образом любому из объектов доступен метод для изменения атрибута base_battery_status
# и любой из объектов всегда будет «знать» актуальное значение этого атрибута.






# Статические методы

# Объявим в классе статический метод predict_battery_lifetime(),
# который будет вычислять прогнозируемый срок работы аккумулятора:
class Robot:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_base_battery_status(cls, new_status):
        cls.base_battery_status = new_status

    def report(self):
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора
        на основе текущей ёмкости и количества циклов зарядки.
        """
        # Пусть максимальная ёмкость нового аккумулятора будет равна 5000 мАч
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)


# Вызов статического метода через имя класса:
battery_lifetime = Robot.predict_battery_lifetime(4000, 100)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {battery_lifetime:.0f} циклов зарядки.'
)


# Создаём объект класса:
robot = Robot('R2-D2')
# Статический метод доступен и в объекте:
r2d2_battery_lifetime = robot.predict_battery_lifetime(3500, 150)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {r2d2_battery_lifetime:.0f} циклов зарядки.'
)





# Из метода в свойство объекта, благодаря декоратору property
class Robot:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_base_battery_status(cls, new_status):
        cls.base_battery_status = new_status

    def report(self):
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора
        на основе текущей ёмкости и количества циклов зарядки.
        """
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)

    @property
    def identifier(self):
        """Вычисляет уникальный идентификатор робота на основе его имени."""
        # Преобразование имени в числовое представление:
        return sum(ord(char) for char in self.name)


# Создаём робота:
robot = Robot('R2-D2')
print(robot.identifier)









# ЗАДАНИЕ 2: декораторы методов класса
# Реализуйте класс Product.
# Атрибуты экземпляра класса: 
# - name — название товара, строка;
# - retail_price — розничная цена, число;
# - purchase_price — закупочная цена, число.

# Методы:
# 1. Свойство profit должно возвращать разницу между розничной и закупочной ценой товара.
# Например, для товара, у которого розничная цена 200, а закупочная — 180, этот метод должен вернуть 20.

# 2. Статический метод average_price(), который принимает список розничных цен нескольких товаров
# и возвращает их среднюю розничную цену. Например, для цен 100, 300 и 800 этот метод должен вернуть число 400.
# При вызове этого метода без аргументов он должен вернуть 0.

# 3. Свойство-метод information должно возвращать строку с информацией о товаре (название, розничная и закупочная цена).
# Например, для товара с названием Шляпа с розничной ценой 1000 и закупочной ценой 800 должна вернуться строка
'Товар: Шляпа, розничная цена: 1000, закупочная цена: 800'


class Product:
    def __init__(self, name, retail_price, purchase_price):
        self.name = name
        self.retail_price = retail_price
        self.purchase_price = purchase_price

    # Опишите свойство profit

    # Опишите статический метод average_price()

    # Опишите свойство information


# Данные для проверки, не изменяйте их.
product_1 = Product('Картошка', 100, 90)
product_2 = Product('Перчатки', 150, 120)
product_3 = Product('Велосипед', 170, 150)

assortment_prices = [
    product_1.retail_price,
    product_2.retail_price,
    product_3.retail_price,
]

print(f'Средняя стоимость: {Product.average_price(assortment_prices)}')
print(f'Прибыль магазина с товара {product_1.name}: {product_1.profit}')
print(f'Информация о товаре {product_1.name}: {product_1.information}')




# ПОДСКАЗКИ
# 1. Для реализации метода profit вам нужно вычесть закупочную цену из розничной.
# 2. Статический метод average_price должен принимать на вход коллекцию чисел и вычислять среднее арифметическое.
# И неважно, что это будут за числа: стоимость товаров, количество страниц в книгах или вес овечек.
# 3. В статическом методе average_price используйте встроенные функции sum() и len() для расчёта средней цены.





# РЕШЕНИЕ
class Product:
    def __init__(self, name, retail_price, purchase_price):
        self.name = name
        self.retail_price = retail_price
        self.purchase_price = purchase_price

    # Опишите свойство profit
    @property
    def profit(self):
        difference = self.retail_price - self.purchase_price
        return difference
    
    # Опишите статический метод average_price()
    @staticmethod
    def average_price(assortment_prices):
        return sum(assortment_prices) / len(assortment_prices)
        
        
    # Опишите свойство information
    @property
    def information(self):
        return (f'Товар: {self.name}, розничная цена: {self.retail_price},'
                f' закупочная цена: {self.purchase_price}')
    
    
# Данные для проверки, не изменяйте их.
product_1 = Product('Картошка', 100, 90)
product_2 = Product('Перчатки', 150, 120)
product_3 = Product('Велосипед', 170, 150)

assortment_prices = [
    product_1.retail_price,
    product_2.retail_price,
    product_3.retail_price,
]

print(f'Средняя стоимость: {Product.average_price(assortment_prices)}')
print(f'Прибыль магазина с товара {product_1.name}: {product_1.profit}')
print(f'Информация о товаре {product_1.name}: {product_1.information}')
