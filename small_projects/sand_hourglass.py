import random
import sys
import time
import bext 

"""
TODO use os module to get WIDTH and HEIGHT for terminal in windows, because thats funny part

"""

PAUSE_LENGTH = 0.2 
WIDE_FALL_CHANSE = 50
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 24


X = 0
Y = 1
SAND = '.'
WALL = '#'
HOURGLASS = set()

for i in range(18, 37):
    HOURGLASS.add((i, 1))  # top
    HOURGLASS.add((i, 23))  # bottom

for i in range(1, 5):
    HOURGLASS.add((18, i))
    HOURGLASS.add((36, i)) 
    HOURGLASS.add((18, i + 19))
    HOURGLASS.add((36, i + 19))
for i in range(8):
    HOURGLASS.add((i + 19, 5 + i))
    HOURGLASS.add((35 - i, 5 + i))
    HOURGLASS.add((25 - i, 13 + i))
    HOURGLASS.add((29 + i, 13 + i))

INITIAL_SEND = set()# starting sand
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SEND.add((x, y + 4))

def main():
    bext.fg('yellow')
    bext.clear()

    bext.goto(0, 0)
    print('Ctrl-C to quit.', end='')

    # Display the hourglass walls
    for wall in HOURGLASS:
        bext.goto(wall[X], wall[Y])
        print(WALL, end='')

    allSand = list(INITIAL_SEND)

    # Display the initial sand
    for sand in allSand:
        bext.goto(sand[X], sand[Y])
        print(SAND, end='')

    run_hour_glass_simulation(allSand)

def run_hour_glass_simulation(allSand):
    '''Modeling sand falling'''

    while True:
        random.shuffle(allSand)

        sand_move_on_this_step = False 
        for i, sand in enumerate(allSand):

            if sand[Y] == SCREEN_HEIGHT - 1:
                continue 

            # Checking if sand can fall directly down
            below = (sand[X], sand[Y] + 1)
            no_sand_below = below not in allSand 
            no_wall_below = below not in HOURGLASS
            can_fall_below = no_sand_below and no_wall_below

            if can_fall_below:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND, end='')

                allSand[i] = (sand[X], sand[Y] + 1)
                sand_move_on_this_step = True 
            else:
                # can sand fall left
                below_left = (sand[X] - 1, sand[Y] + 1)
                no_sand_below_left = below_left not in allSand
                no_wall_below_left = below_left not in HOURGLASS 

                left = (sand[X] - 1, sand[Y])
                no_wall_left = left not in HOURGLASS
                not_on_left_edge = sand[X] > 0
                can_fall_left = (no_sand_below_left and no_wall_below_left
                                 and no_wall_left and not_on_left_edge)
                
                # can sand fall right
                below_right = (sand[X] + 1, sand[Y] + 1)
                no_sand_below_right = below_right not in allSand
                no_wall_below_right = below_right not in HOURGLASS

                right = (sand[X] + 1, sand[Y])
                no_wall_right = right not in HOURGLASS
                not_on_right_edge = sand[X] < SCREEN_WIDTH - 1
                can_fall_right = (no_sand_below_right and no_wall_below_right 
                                  and not_on_right_edge and no_wall_below_right)
                
                # pick a direction
                falling_direction = None 
                if can_fall_left and not can_fall_right:
                    falling_direction = -1 # left
                elif not can_fall_left and can_fall_right:
                    falling_direction = 1 # right
                elif can_fall_left and can_fall_right:
                    falling_direction = random.choice([-1, 1])

                # check if sand can fall for 2 positions right or left
                if random.random() * 100 <= WIDE_FALL_CHANSE:
                    below_two_left =  (sand[X] - 2, sand[Y] + 1)
                    no_sand_below_two_left =  below_two_left not in allSand
                    no_wall_below_two_left = below_two_left not in HOURGLASS
                    not_on_second_two_left = sand[X] > 1
                    can_fall_two_left = (can_fall_left and no_sand_below_two_left
                                         and no_wall_below_two_left and not_on_second_two_left)

                    below_two_right = (sand[X] + 2, sand[Y] + 1)
                    no_sand_below_two_right = below_two_right not in allSand
                    no_wall_below_two_right = below_two_right not in HOURGLASS
                    not_on_second_two_right = sand[X] < SCREEN_WIDTH - 2
                    can_fall_two_right = (can_fall_two_left and no_sand_below_two_right
                                          and no_wall_below_two_right and not_on_second_two_right)
                    
                    if can_fall_two_left and not can_fall_two_right:
                        falling_direction = -2

                    elif not can_fall_two_left and can_fall_two_right:
                        falling_direction = 2
                    elif can_fall_two_left and can_fall_two_right:
                        falling_direction = random.choice([-2, 2])

                if falling_direction is None:
                    continue 
                
                # Update sand position if falling direction is set
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
                bext.goto(sand[X] + falling_direction, sand[Y] + 1)
                print(SAND, end='')

                # move sand to new place
                allSand[i] = (sand[X] + falling_direction, sand[Y] + 1)
                sand_move_on_this_step = True

        sys.stdout.flush()
        time.sleep(PAUSE_LENGTH)

        if not sand_move_on_this_step:
            time.sleep(2)

            for sand in allSand:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break


if __name__ == '__main__':
    try :
        main()
    except KeyboardInterrupt:
        sys.exit()




