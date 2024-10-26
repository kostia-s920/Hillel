import re


def is_palindrome(text):

    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

    # Перевіряємо, чи є очищений рядок паліндромом
    return cleaned_text == cleaned_text[::-1]


# Тести з виведенням результатів
print("Test1:", is_palindrome('A man, a plan, a canal: Panama'))
print("Test2:", is_palindrome('0P'))
print("Test3:", is_palindrome('a.'))
print("Test4:", is_palindrome('aurora'))

#
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
