def correct_sentence(sentence1, sentence2):
    if not sentence1.endswith('.'):
        sentence1 += '.'
        sentence1 = sentence1.capitalize()
    if not sentence2.endswith('.'):
        sentence2 += '.'
        sentence2 = sentence2.capitalize()
    final_sentence = sentence1 + " " + sentence2
    return final_sentence


assert correct_sentence("greetings, friends","welcome to the event") == "Greetings, friends. Welcome to the event.", 'Test1'
assert correct_sentence("hello", "this is a test") == "Hello. This is a test.", 'Test2'
assert correct_sentence("Greetings.", "Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.", "Have a good day.") == "Greetings, friends. Have a good day.", 'Test4'
assert correct_sentence("hi there", "how are you") == "Hi there. How are you.", 'Test5'

print('ОК')
