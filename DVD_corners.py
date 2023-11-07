import sys, random, time
import bext

WIDTH, HEIGHT = bext.size()
# В Windows нельзя вывести символ в последний столбец без добавления
  # автоматически символа новой строки, так что уменьшаем ширину на 1:
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                     X: random.randint(1, WIDTH - 4),
                     Y: random.randint(1, HEIGHT - 4),
                     DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
    cornerBounses = 0
    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print(' ', end='')

            originalDirection = logo[DIR]
            if logo[X] and logo [Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounses += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] == UP_RIGHT
                cornerBounses += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounses += 1
            elif logo[X] == WIDTH -3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounses += 1
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            

            # Проверяем, не отскакивает ли логотип от правого края:
            # (WIDTH - 3, поскольку 'DVD' состоит из трех букв.)

            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH -3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH -3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            elif logo[Y] == HEIGHT -1 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == HEIGHT -1 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            elif logo[Y] == HEIGHT -1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == HEIGHT -1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_RIGHT

            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)

            
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1
        bext.goto(5, 0)
        bext.fg('white')
        print('Courner bounces:', cornerBounses, end='')

        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD logo')
        sys.exit()

