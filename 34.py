class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value
        print(f"Ініціалізація лічильника: поточне значення={self.current}, мінімум={self.min_value}, максимум={self.max_value}")

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError("Початкове значення повинно бути в межах мінімуму та максимуму")
        self.current = start
        print(f"Встановлено поточне значення: {self.current}")

    def set_max(self, max_value):
        if max_value < self.min_value:
            raise ValueError("Максимальне значення повинно бути більше мінімального")
        self.max_value = max_value
        print(f"Встановлено максимальне значення: {self.max_value}")

    def set_min(self, min_value):
        if min_value > self.max_value:
            raise ValueError("Мінімальне значення повинно бути менше максимального")
        self.min_value = min_value
        print(f"Встановлено мінімальне значення: {self.min_value}")

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1
        print(f"Збільшено значення: {self.current}")

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1
        print(f"Зменшено значення: {self.current}")

    def get_current(self):
        print(f"Поточне значення: {self.current}")
        return self.current

# Приклади використання та перевірки
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()  #
except ValueError as e:
    print(e)  #
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()
except ValueError as e:
    print(e)
assert counter.get_current() == 7, 'Test4'