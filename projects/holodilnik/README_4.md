# Узнать количество продукта: функция amount()

Один и тот же продукт мог быть закуплен несколько раз, в результате словарь goods будет хранить информацию о нескольких партиях этого продукта:
```python
goods = {
    'Морковь': [  # Продукт "Морковь" покупали дважды:
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 8, 6)}
    ]
}
```
Функция amount() предназначена для определения количества продукта с заданным названием. 
Эта функция должна вернуть число: общее количество продуктов, названия которых частично или полностью совпадают со строкой, переданной в параметры.


### Параметры функции amount()
У функции amount() должно быть два параметра:
    amount(items, needle) 

1. items — словарь, который хранит список продуктов (goods).
2. needle — строка для поиска продукта. Поиск должен быть нечувствителен к регистру.

### Возвращаемое значение
Функция возвращает общее количество запрошенного продукта — число типа Decimal.


### Пример объявления и использования
```python
import datetime
from decimal import Decimal

goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': None}],
    'Морковь': [
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2023, 8, 6)}
    ],
    'Вода': [{'amount': Decimal('2.5'), 'expiration_date': None}]
}

def amount(items, needle):
    pass

print(amount(goods, 'яйца'))
# Вывод: 1
print(amount(goods, 'морковь'))
# Вывод: 5
```