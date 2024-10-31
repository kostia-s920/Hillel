def difference(*args):
    # Якщо аргументів немає, повертаємо 0
    if not args:
        return 0

    # Обчислюємо різницю між максимальним і мінімальним значенням
    diff = max(args) - min(args)

    # Округлюємо результат до 2 десяткових знаків
    return round(diff, 2)


# Тести з виведенням результатів
print("Test1:", difference(1, 2, 3))  # Очікується 2
print("Test2:", difference(5, -5))  # Очікується 10
print("Test3:", difference(10.2, -2.2, 0, 1.1, 0.5))  # Очікується 12.4
print("Test4:", difference())  # Очікується 0

# Перевірка через assert
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'

