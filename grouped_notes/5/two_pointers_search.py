
def find_two_indexes(data, expected_result):
    # В начале работы 
    # - левый указатель указывает на первый элемент списка (с индексом 0):
    left_pointer = 0
    # - правый указатель указывает на последний элемент списка. 
    # Индекс этого элемента на единицу меньше длины списка.
    right_pointer = len(data) - 1
    # Пока индекс левого указателя меньше индекса правого указателя.
    while data[left_pointer] < data[right_pointer]:
        if data[left_pointer] + data[right_pointer] == expected_result:
            return ((left_pointer, right_pointer), (data[left_pointer], data[right_pointer]))
        # Считаем сумму двух элементов.
        # Если она совпадает с искомой...
        
            # ...возвращаем ответ:
        elif data[left_pointer] + data[right_pointer] > expected_result:
            right_pointer -= 1
        # Если сумма больше искомой, то...
        
            # ...надо уменьшить сумму: уменьшаем значение правого указателя.
        else:
            left_pointer += 1
        # Все остальные варианты относятся к случаям, когда сумма меньше искомой. 
        
            # Сумму надо увеличить, для этого увеличиваем значение левого указателя.
            


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 4
    print(find_two_indexes(data, expected_result))

    