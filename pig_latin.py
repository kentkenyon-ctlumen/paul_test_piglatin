"""
pig_latin.py
"""

def pig_latin(word):
    """
    Input: string, in the form of a single word
    Output: a word "translated" into pig latin
    """
    if word.isalpha():
        word_lower = word.lower()
        consonants = 'bcdfghjklmnopqrstvwxyz'
        if word_lower[:1] in consonants:
            translated_word = str(word_lower[1:]) + str(word_lower[:1]) + 'ay'
        else:
            translated_word = word + 'ay'
        print(translated_word.lower())
    else:
        print("Please provide a valid word. Make sure you do not include spaces, numbers, or special characters.")


user_input = ""
while user_input != "exit":
    user_input = input("Please enter a single word with no spaces to be translated!\n")
    for word in user_input.split():
        pig_latin(word)
