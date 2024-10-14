import string

input_string = input("Введіть рядок: ")

# Видаляємо всі символи пунктуації
cleaned_string = ''.join(char for char in input_string if char not in string.punctuation)

# Розбиваємо рядок на слова і перетворюємо кожне слово з великої літери
words = cleaned_string.split()
capitalized_words = ''.join(word.capitalize() for word in words)

# Додаємо хештег на початок
hashtag = '#' + capitalized_words

# Якщо довжина хештега більше 140 символів, обрізаємо його
if len(hashtag) > 140:
    hashtag = hashtag[:140]

# Виводимо результат
print(hashtag)