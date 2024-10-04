numbers = [1, 2, 3]

# Якщо список порожній
if len(numbers) == 0:
    result = [numbers]
# Якщо в списку один елемент
elif len(numbers) == 1:
    result = [numbers]
else:
    last_number = numbers[len(numbers) - 1]  # Отримуємо останній елемент списку
    numbers.insert(0, last_number)    # Вставляємо останній елемент на початок списку
    numbers = numbers[:-1]                   # Видаляємо останній елемент зі списку
print(numbers)