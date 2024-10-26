def find_unique_value(some_list):
    counts = {}

    # Підраховуємо кількість входжень кожного числа
    for number in some_list:
        counts[number] = counts.get(number, 0) + 1

    # Знаходимо число, яке зустрічається тільки один раз
    for number, count in counts.items():
        if count == 1:
            return number


# Тести з виведенням результатів
print("Test1:", find_unique_value([1, 2, 1, 1]))  # Очікується 2
print("Test2:", find_unique_value([2, 3, 3, 3, 5, 5]))  # Очікується 2
print("Test3:", find_unique_value([5, 5, 5, 2, 2, 0.5]))  # Очікується 0.5

#
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'

print("ОК")
