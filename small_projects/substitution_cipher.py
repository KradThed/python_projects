import pyperclip
import random 


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    while True:
        print('(e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()

        if response.startswith('e'):
            my_mode = 'encrypt'
            break 
        elif response.startswith('d'):
            my_mode = 'decrypt'
            break 
        print('e or d ?')

    while True: 
        print('Specify the key to use')
        if my_mode == 'encrypt':
            print('Or enter RANDOM to have one generated')
        response = input('> ').upper()
        if response == 'RANDOM':
            m_key = generate_random_key()
            print(f'The key is {m_key} keep it in secret!')
            break 
        else:
            if check_key(response):
                m_key = response 
                break 
    print('Enter message')
    my_message = input()

    if my_mode == 'encrypt':
        translated = encrypt_message(my_message, m_key)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_message, m_key)
    
    print(f'The {my_mode} message')
    print(translated)

    try:
        pyperclip.copy(translated)
        print(f'Full {my_mode} message copied to clipboard')
    except:
        pass

def check_key(key):
    key_list = list(key)
    letter_list = list(LETTERS)
    key_list.sort()
    letter_list.sort()

    if key_list != letter_list:
        print('Problem with set or key')
        return False 
    return True 

def encrypt_message(message, key):
    return translate_message(message, key, 'encrypt')

def decrypt_message(message, key):
    return translate_message(message, key, 'decrypt')

def translate_message(message, key, mode):
    translated = ''
    charsA = LETTERS
    charsB = key 
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA 
    
    for symbol in message:
        if symbol.upper() in charsA:
            sym_index = charsA.find(symbol.upper())
            
            if symbol.isupper():
                translated += charsB[sym_index].upper()
            else:
                translated += charsB[sym_index].lower()
            
        else:
            translated += symbol 
    return translated 

def generate_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
        main()

   
    
        


"""
403 291 461 126 605 635 584 000 000 possible variations

"""

