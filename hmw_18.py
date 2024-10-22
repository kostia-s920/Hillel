def common_elements():
    # Генеруємо множину чисел, кратних 3
    multiples_of_3 = {i for i in range(100) if i % 3 == 0}

    # Генеруємо множину чисел, кратних 5
    multiples_of_5 = {i for i in range(100) if i % 5 == 0}

    common = multiples_of_3 & multiples_of_5

    return common

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test failed'

print("ОК")