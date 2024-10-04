numbers = [1, 2, 3, 4, 5]

if (len(numbers) % 2) == 0:
    # Якщо кількість елементів парна
    first_part = numbers[:len(numbers) // 2]
    second_part = numbers[len(numbers) // 2:]
    result = [first_part, second_part]
elif len(numbers) == 0:
    # Якщо список порожній
    result = [[], []]
elif len(numbers) == 1:
    # Якщо в списку лише один елемент
    result = [numbers, []]
else:
    # Якщо кількість елементів непарна
    first_part = numbers[:len(numbers) // 2 + 1]
    second_part = numbers[len(numbers) // 2 + 1:]
    result = [first_part, second_part]
print(result)







