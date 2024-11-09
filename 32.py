class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}  # Словник для зберігання товарів та їх кількості

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self):
        total = sum(item.price * count for item, count in self.products.items())
        return total

    def __str__(self):
        result = f"User: {self.user}\nItems:\n"
        for item, count in self.products.items():
            result += f"{item.name}: {count} pcs.\n"
        result += f"Total cost: {self.get_total()}"
        return result

# Створення екземплярів товарів
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)

# Створення екземпляра покупця
buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

# Створення замовлення та додавання товарів
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

# Перевірки
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

# Додавання додаткових товарів і перевірка
cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 10)

print(cart)

assert cart.get_total() == 40, "Повинно залишатися 40!"