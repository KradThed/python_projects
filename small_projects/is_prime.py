import math
import sys 
import random 

"""
Print n prime numbers including(if n is prime) or after n
"""

def main():
    num = random.randint(1, 1000)
    print(num)
    prime_counter = 0 

    while prime_counter < 10:
        if isPrime(num):
            print(str(num) + ', ', end='', flush=True)
            prime_counter += 1
        num += 1

def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True 

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False 
    return True 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() 

    
        
