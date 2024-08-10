import sevseg
import sys, time

def format_digit(digit_str):
    return f'\033[1;34m{digit_str}\033[0m'

def format_separator():
    return '\033[1;31m:\033[0m'

try:
    while True:
        print('\n' * 60)
        current_time = time.localtime()
        hours = str(current_time.tm_hour % 12)
        if hours == '0':
            hours = '12'
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

        hDigits = sevseg.getSevSegStr(hours, 2)
        mDigits = sevseg.getSevSegStr(minutes, 2)
        sDigits = sevseg.getSevSegStr(seconds, 2)

        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Format and print the clock
        print(f' \033[1;33m+---------------------+\033[0m ')
        print(f' | {format_digit(hTopRow)} * {format_digit(mTopRow)} * {format_digit(sTopRow)} | ')
        print(f' | {format_digit(hMiddleRow)} {format_separator()} {format_digit(mMiddleRow)} {format_separator()} {format_digit(sMiddleRow)} | ')
        print(f' | {format_digit(hBottomRow)} {format_separator()} {format_digit(mBottomRow)} {format_separator()} {format_digit(sBottomRow)} | ')
        print(f' \033[1;33m+---------------------+\033[0m ')
        print()
        print('Press Ctrl-C to quit.')

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != current_time.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital clock')
    sys.exit()
