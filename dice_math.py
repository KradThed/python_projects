import random, time

DICE_WIDTH = 9
DICE_HEIGHT = 7
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3

QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = 1

assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print(f'''Dice math with ASCII graphics
      Add up the sides of all the dice displayed on the screen. You have
      {QUIZ_DURATION} seconds to answer as many as possible. You get {REWARD} points for each
      correct answer and lose {PENALTY} point for each incorrect answer.
      ''')
input('Press Enter to begin...')

correct_answers = 0
incorrect_answers = 0
startTime = time.time()

while time.time() < startTime + QUIZ_DURATION:
    sumAnswer = 0
    dice_faces = []

    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        dice = random.choice(ALL_DICE)
        dice_faces.append(dice[0])
        sumAnswer += dice[1]

    top_left_dice_corner = []

    for i, die_face in enumerate(dice_faces):
        while True:
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            top_left_x = left
            top_left_y = top
            top_right_x = left + DICE_WIDTH
            top_right_y = top
            bottom_left_x = left
            bottom_left_y = top + DICE_HEIGHT
            bottom_right_x = left + DICE_WIDTH
            bottom_right_y = top + DICE_HEIGHT

            overlaps = False
            for prev_dice_left, prev_dice_top in top_left_dice_corner:
                prev_dice_right = prev_dice_left + DICE_WIDTH
                prev_dice_bottom = prev_dice_top + DICE_HEIGHT

                if (top_left_x < prev_dice_right and top_right_x > prev_dice_left
                    and top_left_y < prev_dice_bottom and bottom_left_y > prev_dice_top):
                    overlaps = True

            if not overlaps:
                top_left_dice_corner.append((left, top))
                break

    canvas = {}
    for i, (prev_dice_left, prev_dice_top) in enumerate(top_left_dice_corner):
        die_face = dice_faces[i]
        for dy in range(len(die_face)):
            for dx in range(len(die_face[dy])):
                canvasX = prev_dice_left + dx
                canvasY = prev_dice_top + dy
                canvas[(canvasX, canvasY)] = die_face[dy][dx]

    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()

    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correct_answers += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrect_answers += 1

score = (correct_answers * REWARD) - (incorrect_answers * PENALTY)

print('Correct: ', correct_answers)
print('Incorrect:', incorrect_answers)
print('Score: ', score)
