# Просимо користувача ввести чотири значне число
number = int(input("Введіть 4-значне число: "))

# Отримуємо тисячі
n1 = number // 1000

# Отримуємо сотні
n2 = (number // 100) % 10

# Отримуємо десятки
n3 = (number % 100) // 10

# Отримуємо одиниці
n4 = number % 10

# Простий варіант виводу
print(n1)
print(n2)
print(n3)
print(n4)

# Другий варіант виводу кожної цифри на новому рядку
# print(n1, n2, n3, n4, sep="\n")