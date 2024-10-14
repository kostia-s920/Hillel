import string
import keyword

test_data = ['.', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value',
             'Get_value', 'get_Value', 'getValue', '3m', 'm3', 'assert', 'assert_exception']

for test_variable in test_data:
    is_correct = True
    print(f"\nПеревірка змінної: {test_variable}")

    # Перевірка на зареєстровані ключові слова
    if test_variable in keyword.kwlist:
        print(f"Error! {test_variable} is a Python keyword!")
        is_correct = False

    # Перевірка на перший символ (не цифра)
    elif test_variable[0].isdigit():
        print(f"Error! {test_variable} cannot start with a digit!")
        is_correct = False

    # Перевірка на наявність великої літери
    elif any(char.isupper() for char in test_variable):
        print(f"Error! {test_variable} contains uppercase letters!")
        is_correct = False

    # Перевірка на наявність пробілів
    elif ' ' in test_variable:
        print(f"Error! {test_variable} contains spaces!")
        is_correct = False

    # Перевірка на заборонені символи (окрім '_')
    elif any(symbol in test_variable for symbol in string.punctuation.replace("_", "")):
        print(f"Error! {test_variable} contains punctuation marks!")
        is_correct = False

    # Перевірка на кількість нижніх підкреслень (не більше одного)
    elif test_variable.count('_') > 1:
        print(f"Error! {test_variable} contains more than one underscore!")
        is_correct = False

    if is_correct:
        print(f"{test_variable} is a valid variable name!")