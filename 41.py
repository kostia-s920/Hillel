import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може дорівнювати нулю.")
        self.a = a
        self.b = b
        self.simplify()

    def simplify(self):
        """Скорочує дріб"""
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        result = Fraction(new_a, new_b)
        return result

    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        result = Fraction(new_a, new_b)
        return result

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        result = Fraction(new_a, new_b)
        return result

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 7, 6', f"Очікувалося 'Fraction: 7, 6', але отримано {str(f_c)}"
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 1, 3', f"Очікувалося 'Fraction: 1, 3', але отримано {str(f_d)}"
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 1, 6', f"Очікувалося 'Fraction: 1, 6', але отримано {str(f_e)}"

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')