from example import Employee, FullTimeEmployee, PartTimeEmployee

# Создаем экземпляры классов
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')

# Тестируем метод get_unpaid_vacation у FullTimeEmployee
print("Тестирование FullTimeEmployee:")
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))

# Тестируем get_vacation_details у PartTimeEmployee
print("\nТестирование PartTimeEmployee:")
print(part_time_employee.get_vacation_details())

# Проверяем значения атрибутов
print(f"\nFullTimeEmployee vacation days: {full_time_employee.remaining_vacation_days}")
print(f"PartTimeEmployee vacation days: {part_time_employee.remaining_vacation_days}")

# Проверяем использование отпуска
print("\nИспользование отпуска:")
full_time_employee.consume_vacation(3)
part_time_employee.consume_vacation(2)

print(full_time_employee.get_vacation_details())
print(part_time_employee.get_vacation_details())