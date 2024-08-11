import math 
import time 
import sys 
import shutil


"""
Using math.sin() generate wave message
"""
WIDTH, HEIGHT = shutil.get_terminal_size()
WIDTH -=1 # test for windows because we cant show something in the last column without adding / 

print('Ctr-c to QUIT')
print()
print(f'What to display? Maximum size from 1 to {WIDTH // 2} chars' )

while True: 
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break 
    print(f'Message must be 1 to {WIDTH //2} characters long')

step = 0.0
# sinus range is -1.0 to 1.0 that is why we need multiplier 
multiplier = (WIDTH - len(message)) / 2
try:
    while True:
        sin_of_step = math.sin(step)
        padding = ' ' * int((sin_of_step + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.1
except KeyboardInterrupt:
    sys.exit()