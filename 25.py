def some_gen(begin, end, func):
    current = begin
    for i in range(end):
        yield current
        print(f"Значення після функції: {current}")
        current = func(current)

# Перевірка
def pow(x):
    return x ** 2

gen = some_gen(2, 4, pow)
print("Результат генератора у вигляді списку:", list(gen))

# Перевірки
from inspect import isgenerator
gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print("ОК")