import random
import time


def display_intro():
    print("'Вы находитесь в землях, заселенных драконами."
    "Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,"
    "оторый готов поделиться с вами своими сокровищами. Во второй —"
    "жадный и голодный дракон, который мигом вас съест")


def choose_cave():
        print("В какую перещу решите войти? 1  или 2?")
        cave = input()
        return cave

def check_cave(choose_cave):
    print('Перед вами неподалеку...!')
    time.sleep(1)
    print('Ее темнота заставляет вас содрогнуться!....')
    time.sleep(1)
    print('И ВОТ ОГРОМНЫЙ ДРАКОН ВЫПРЫГИВАЕТ НА ВАС!')
    print()
    time.sleep(1)
    friendly_cave = random.randint(1, 2)
    if int(choose_cave) == friendly_cave: 
        print('Он поделился с вами сокровищами\n')
    else:
        print('Из вас вышел неплохой обед\n')  
        

play_again = 'yes'
while play_again.lower() == 'yes' or play_again.lower() == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(int(cave_number))  # Convert the input to an integer
    print('Wanna try again? yes or not')
    play_again = input()



