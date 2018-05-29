"""
Cisco Black Belt: programability Level 1
Number guessing game
submitted by: Vaibhav Solanki(vaibhav.solanki@agcnetworks.com)
"""

import random
while(True):
    num = random.randint(1,10)
    print(num)
    guess = int(input())
    if guess == num:
        print("Correct!")
        break
    else:
        print('Wrong, try again!')
