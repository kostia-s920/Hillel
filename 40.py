import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_area = self.get_square() + other.get_square()
        new_width = self.width  # Використовуємо ширину першого прямокутника
        new_height = new_area / new_width  # Вираховуємо висоту
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.get_square() * n
        new_width = self.width  # Зберігаємо ширину
        new_height = new_area / new_width  # Вираховуємо нову висоту
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle(width={self.width:.2f}, height={self.height:.2f}, area={self.get_square():.2f})"

# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

# Перевірка площі
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

# Додавання
r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

# Множення
r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

# Порівняння
assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

# Вивід результатів
print(r1)
print(r2)
print(r3)
print(r4)