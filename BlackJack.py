import random
import sys

#Realise BlackJack in python
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'

def main():
    print('''
    Blackjack
    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.
    ''')

    money = 5000
    while True:
        if money <= 0:
            print('You are out of money')
            print("That's not bad since you weren't playing with real money")
            print('Thanks for playing')
            sys.exit()

        print('Money:', money)
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet:', bet)
        while True:
            display_hands(playerHand, dealerHand, False)
            print()

            if get_hand_value(playerHand) > 21:
                break

            move = getMove(playerHand, money)

            if move == 'D':
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if get_hand_value(playerHand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if get_hand_value(playerHand) <= 21:
            while get_hand_value(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                display_hands(playerHand, dealerHand, False)

                if get_hand_value(dealerHand) > 21:
                    break

            input('Press enter to continue...')
            print('\n')

        display_hands(playerHand, dealerHand, True)

        playerValue = get_hand_value(playerHand)
        dealerValue = get_hand_value(dealerHand)

        if dealerValue > 21:
            print('Dealer busts! You win {}'.format(bet))
            money += bet
        elif playerValue > 21 or playerValue < dealerValue:
            print('You lost!')
            money -= bet
        elif playerValue > dealerValue:
            print('You won {}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('Draw!')
        input('Press enter to continue...')
        print('\n')

def getBet(maxBet):
    while True:
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT' or bet == 'Q':
            print('Thanks for playing')
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def display_hands(playerHand, dealerHand, showDealerHand):
    print('')
    if showDealerHand:
        print('DEALER', get_hand_value(dealerHand))
        display_cards(dealerHand)
    else:
        print('Dealer: ???')
        display_cards([BACKSIDE] + dealerHand[1:])

    print('PLAYER', get_hand_value(playerHand))
    display_cards(playerHand)

def get_hand_value(cards):
    numberOfAces = 0
    value = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def display_cards(cards):
    rows =  ['', '', '', '', '']

    for i, card in enumerate(cards):
        rows[0] += '____'
        if card == BACKSIDE:
            rows[1] +=  '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move

        if move == 'D' and '(D)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()
