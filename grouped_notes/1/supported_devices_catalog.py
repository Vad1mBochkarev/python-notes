# ЗАДАНИЕ ИТОГОВОЕ
# Ваша задача — разработать систему для работы сервисного центра всемирно известной компании "Cucumber". Она выпускает мобильные гаджеты и устройства для «умного дома».
# Полный перечень техники производства "Cucumber" c указанием модельного ряда содержится в словарях mobile_devices и home_devices.
# Каждый день компания присылает перечень устройств, поддержка которых прекращена. Перечень хранится в множестве not_supported_devices.
# Задача программы — заполнить словарь result_catalog: в него должны попасть только те устройства, поддержку которых компания не прекратила. Ключами словаря должны быть названия устройств, а значениями — годы выпуска, например, 'cucuEar': 2018.

# Выведите на экран строку 'Каталог поддерживаемых девайсов:'; на следующей строке напечатайте словарь result_catalog. 

# Должно получиться примерно так:
    # "Каталог поддерживаемых девайсов:"
    # {'cucuLot': 2011, 'cucuMonitor': 2020, 'cucuEar': 2018, ...} 


mobile_devices = {
    'cucuPhone': 2010,
    'cucuBlet': 2013,
    'cucuClock': 2015,
    'cucuEar': 2018,
    'cuCube': 2015,
}

home_devices = {
    'cucuLot': 2011,
    'cucuBlock': 2010,
    'cucuWall': 2010,
    'cucuMonitor': 2020,
    'cucuLamp': 2015,
    'cucuTable': 2016,
    'cucuTV': 2017,
}

not_supported_devices = {'cucuBlock', 'cucuBlet', 'cucuWall'}
result_catalog = {}

mobile_devices.update(home_devices)

all_devices = mobile_devices 

for device, year in all_devices.items():
    if device not in not_supported_devices:
        result_catalog[device] = year

print('Каталог поддерживаемых девайсов:')
print(result_catalog)
