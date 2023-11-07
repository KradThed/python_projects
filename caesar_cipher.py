import pyperclip

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d')

while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Please enter the key (0) to {maxKey} to use.')
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

print(f'Enter the message to {mode}')
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)  # Get the numeric value of the symbol
        if mode == 'encrypt':
            num = (num + key) % len(SYMBOLS)
        elif mode == 'decrypt':
            num = (num - key) % len(SYMBOLS)
        translated += SYMBOLS[num]
    else:
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard')
except:
    pass