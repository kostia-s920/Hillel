def is_even(digit):
    """ Перевірка чи є парним число """
    print(f"Число для перевірки: {digit}")  # Виводимо вхідне число
    result = digit % 2 == 0
    print(f"Чи є число {digit} парним? {result}")  # Виводимо результат перевірки
    return result



# Перевірка через assert
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print("OK")