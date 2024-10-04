number1 = int(input("Enter number 1 :"))
number2 = int(input("Enter number 2 :"))
sign = input("Enter sign (+, -, *, /) :")

if sign == '+':
    result = number1 + number2              # Якщо знак '+', додаємо два числа
elif sign == '-':
    result = number1 - number2              # Якщо знак '-', віднімаємо друге число від першого
elif sign == '*':
    result = number1 * number2              # Якщо знак '*', множимо два числа
elif sign == '/' and number2 != 0:
    result = number1 / number2              # Якщо знак '/' і друге число не нуль, ділимо перше число на друге
else:
    result = "Incorrect insert data"        # Якщо введено некоректні дані або ділення на нуль, виводимо повідомлення
print(result)