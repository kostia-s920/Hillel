
def generate_cube_numbers(end):
    n = 2
    while True:
        cube = n ** 3
        print(f"Число: {n}, Куб: {cube}")  # Виводимо поточне число і його куб
        if cube > end:
            return
        yield cube
        n += 1

# Тести з виведенням результатів
from inspect import isgenerator

gen = generate_cube_numbers(1)
print("Test0:", "isgenerator(gen) =", isgenerator(gen))
print("Test1:", list(generate_cube_numbers(10)))
print("Test2:", list(generate_cube_numbers(100)))
print("Test3:", list(generate_cube_numbers(1000)))


assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print('OK')