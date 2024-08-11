import  pyperclip 
"""
ROT13 cipher

"""


UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS =  'abcdefghijklmnopqrstuvwxyz'

while True:
    message = input('> ')

    if message.upper == 'QUIT':
        break 
    translated = ''

    for character in message:
        if character.isupper():
            trans_char_index = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[trans_char_index]
        elif character.islower():
            trans_char_index = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[trans_char_index]
        else:
            translated += character

    print('The translated message is:')
    print(translated)
    print()

    try:
        pyperclip.copy(translated)
        print('Copied to clipboard!')
    except:
        pass