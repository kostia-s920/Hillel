def add_one(some_list):
    # Перетворюємо список цифр на ціле число
    number = int(''.join(map(str, some_list)))

    # Додаємо 1 до числа
    number += 1

    # Перетворюємо число назад на список цифр і повертаємо результат
    result = [int(digit) for digit in str(number)]
    print(f"Результат у вигляді списку цифр: {result}")

    return result


# Тести
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
