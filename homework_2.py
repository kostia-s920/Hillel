# Просимо користувача ввести пʼяти значне число
number = int(input("Введіть 5-значне число: "))

# Витягуємо першу цифру
n1 = number // 10000

# Витягуємо другу цифру шляхом ділення на 1000 і взяття залишку від ділення на 10
n2 = (number // 1000) % 10

# Витягуємо третю цифру шляхом ділення на 100 і взяття залишку від ділення на 10
n3 = (number // 100) % 10

# Витягуємо четверту цифру шляхом взяття залишку від ділення на 100 і ділення на 10
n4 = (number % 100) // 10

# Витягуємо п'яту цифру шляхом взяття залишку від ділення на 10
n5 = number % 10

# Виводимо цифри числа у зворотному порядку
print(f"{n5}{n4}{n3}{n2}{n1}")