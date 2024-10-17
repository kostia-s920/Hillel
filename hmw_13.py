seconds_input = int(input("Введіть секунди: "))

# Константи для переведення секунд у дні, години, хвилини
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE
SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR

# Обчислюємо кількість днів, годин, хвилин та секунд
days, remaining_seconds = divmod(seconds_input, SECONDS_IN_DAY)
hours, remaining_seconds = divmod(remaining_seconds, SECONDS_IN_HOUR)
minutes, seconds = divmod(remaining_seconds, SECONDS_IN_MINUTE)


if days == 1:
    day_word = "день"
else:
    day_word = "дні" if 2 <= days <= 4 else "днів"


hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)


print(f"{days} {day_word}, {hours_str}:{minutes_str}:{seconds_str}")