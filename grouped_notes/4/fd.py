from decimal import Decimal

goods = {
    'Яйца': [{'amount': Decimal('1'), 'expiration_date': None}],
}


print(goods['Яйца'][0]['amount'])