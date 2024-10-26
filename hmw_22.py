def popular_words(text, words):
    # Перетворюємо текст у нижній регістр і розбиваємо на слова
    words_in_text = text.lower().split()


    # Створюємо словник, де ключі — шукані слова, а значення — їх частота в тексті
    word_count = {}
    for word in words:
        count = words_in_text.count(word)
        word_count[word] = count
        print(f"Шукане слово: '{word}', кількість входжень: {count}")

    return word_count


# Перевірка
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

