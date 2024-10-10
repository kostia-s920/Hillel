lst = [0, 1, 7, 2, 4, 8]

if lst:
    a = 0
    b = max(lst)
    for number in range(len(lst)):
        if number % 2 == 0:
            a += lst[number]
    result = a*b
else:
    result = lst
print(result)