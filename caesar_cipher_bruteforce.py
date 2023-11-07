print('Enter the encrypted message here')
message = input('> ')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):  # Проходим в цикле по всем возможным ключам.
    translated = ''
    # Расшифровываем каждый символ в сообщении:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key 
            # Выполняем переход по кругу, если число меньше 0:
            if num < 0:
                num = num + len(SYMBOLS)
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print(f'Key is #{key}: {translated}')

