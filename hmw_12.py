import string


input_string = input("Введіть дві літери через дефіс (наприклад, a-c): ")


letters = string.ascii_letters

# Розбиваємо введений рядок на дві літери
start_letter, end_letter = input_string.split('-')

# Отримуємо індекси початкової та кінцевої літери
start_index = letters.index(start_letter)
end_index = letters.index(end_letter)


result = letters[start_index:end_index + 1]
print(result)