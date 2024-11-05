
def is_even(number):
    bitwise_result = number & 1
    print(f"Число: {number}, Побітовий результат (number & 1): {bitwise_result}")
    return bitwise_result == 0

# Тести з виведенням результатів
print("Test1:", is_even(2494563894038**2))
print("Test2:", is_even(1056897**2))
print("Test3:", is_even(24945638940387**3))

