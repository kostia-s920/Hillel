while True:
    try:
        # Запитуємо користувача на введення двох чисел і оператора
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Помилка: ділення на нуль!")
                continue
        else:
            print("Невірний оператор!")
            continue


        print(f"Результат: {result}")

    except ValueError:
        print("Помилка: введено нечислове значення!")
        continue

    # Запитуємо користувача, чи хоче він продовжити
    while True:
        continue_calc = input("Бажаєте продовжити? (y/n): ").lower()
        if continue_calc == 'y':
            break
        elif continue_calc == 'n':
            print("Роботу калькулятора завершено.")
            exit()  
        else:
            print("Введіть 'y' для продовження або 'n' для завершення.")