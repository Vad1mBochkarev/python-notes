from datetime import date, datetime as dt, timedelta
from decimal import Decimal

goods = {}
DATE_FORMAT = '%Y-%m-%d'

def add(items, title, amount, expiration_date=None): # items - словарь title - продукт amopunt - кол-во expiration_date - срок годности
    best_before_date = dt.strptime(expiration_date, DATE_FORMAT) if expiration_date else None

    if title in items:
        items[title].append({'amount': Decimal(amount), 'expiration_date': best_before_date})
    else:
        items[title] = [{'amount': Decimal(amount), 'expiration_date': best_before_date}]

def add_by_note(items, note):
    new_note = str.split(note, ' ')
    new_note = [new_note[0] + ' ' + new_note[1], new_note[2], new_note[3]]
    add(items, new_note[0], new_note[1], new_note[2])

def find(items, needle):
    rez = []
    for key in items:
        if key.find(needle) != -1:
            rez.append(key)
    return rez

def amount(items, needle):
    return items[needle][0]['amount']

def expire(items, in_advance_days=0):
    rez = []
    target_date = date.today() + timedelta(days=in_advance_days)
    for key in items:
        for i in items[key]:
            if items[key][i]['expiration_date'] <= target_date:
                rez.append((items[key][i]['amount'], items[key][i]['expiration_date']))
            
    return rez

def expire(items, in_advance_days=0):
    rez = []
    target_date = date.today() + timedelta(days=in_advance_days)
    for title in items:
        for batch in items[title]:
            if batch['expiration_date']:
                exp_date = batch['expiration_date'].date() 
                if exp_date <= target_date:
                    rez.append((title, batch['amount']))
    return rez


add(goods, 'Яйца', Decimal('10'), '2023-9-30')
add(goods, 'Яйца', Decimal('3'), '2023-10-15')
add(goods, 'Вода', Decimal('2.5'))
add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
print(goods)

print(find(goods, 'йц'))

print(amount(goods, 'Яйца'))

print(expire(goods, 1))