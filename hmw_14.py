number = int(input("Enter your number:"))

while number > 9:
    result = 1
    while number > 0:
        num = number % 10
        number = number // 10
        result = result * num
    number = result
print(number)