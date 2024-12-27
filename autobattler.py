import pyautogui
import pydirectinput
import time
from routines import save_routine

import sys
import os

encounter_rate = 22
enemy_per_ecounter = 2.44

clear = lambda: os.system('clear')
wls = pyautogui.getWindowsWithTitle("Final Fantasy IX")

if wls == []:
    print('Game not found')
    sys.exit(0)

print('Game found')

w = wls[0]
w.activate()

print('Windows Focused')

print('AutoBattler Started')

pydirectinput.keyDown('right')

print(f'Battling...')

#save_routine()
count = 1
start_time = time.time()
while True:

    pydirectinput.press('x')
    pydirectinput.press('x')
    pydirectinput.press('x')
    
    measure = time.time()
    if measure - start_time > 600:
        print('Ten minutes lapsed, saving up')
        save_routine()
        start_time = time.time()

        estimate = encounter_rate * enemy_per_ecounter * count
        count = count + 1
        print('Estimated enemy defetated: ', estimate)

        print(f'Battling...')
        
print('AutoBattler Stopped')



