lst = [1, 0, 13, 0, 0, 0, 5]
a = []
b=[]

for number in lst:
    if number != 0:
        a += [number]
    else:
        b += [number]
result = a + b
print(result)