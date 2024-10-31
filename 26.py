import re

def first_word(text):

    match = re.search(r"[a-zA-Z']+", text)
    print(f"Вхідний текст: {text}")
    if match:
        print(f"Перше знайдене слово: {match.group(0)}")
        return match.group(0)
    return ""

# Тести
print("Test1:", first_word("Hello world"))
print("Test2:", first_word("greetings, friends"))
print("Test3:", first_word("don't touch it"))
print("Test4:", first_word(".., and so on ..."))
print("Test5:", first_word("hi"))
print("Test6:", first_word("Hello.World"))