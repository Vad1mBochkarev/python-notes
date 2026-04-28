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
    @property
    def profit(self):
        return self.retail_price - self.purchase_price

    # Опишите статический метод average_price()
    @staticmethod
    def average_price(a):
        if len(a) == 0:
            return 0
        return sum(a) / len(a)

    # Опишите свойство information
    @property
    def information(self):
        return f"Товар: {self.name}, розничная цена: {self.retail_price}, закупочная цена: {self.purchase_price}"


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