import sys, random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('Cho-han game ')

print('''
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse = 5000
print(f'You have {purse} won. How much do you bet? (or type QUIT)')
while True:
    pot = input('> ')
    if pot.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    elif not pot.isdecimal():
        print('Pls enter the number')
    elif int(pot) > purse:
        print('You do not have enought purse to make a bet')
    else:
        pot = int(pot)
        break
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print('The dealer swirls the cup and you hear the rattle of dice.')
print('The dealer slams the cup on the floor, still covering the')
print('dice and asks for your bet.')
print()
print(' CHO (even) or HAN (odd)?')

while True:
    bet = input('> ').upper()
    if bet != 'CHO' and bet != 'HAN':
        print('Please enter either CHO or HAN')
        continue
    else:
        break
print('The dealer lifts the cup to reveal:')
print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
print(' ', dice1, '-', dice2)

rollIssEven = (dice1 + dice2) % 2 == 0
if rollIssEven:
    correctBet = 'CHO'
else:
    correctBet = 'HAN'

playerWon = bet == correctBet

if playerWon :
    print('You won! You take', pot, 'mon.')
    purse = purse + pot 
    print('The house collects a', pot // 10, 'mon fee.')
    purse = purse - (pot // 10) 
else:
    purse = purse - pot
    print('You lost!')

if purse == 0:
    print('You have run out of money!')
    print('Thanks for playing!')
    sys.exit()


