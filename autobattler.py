import argparse
import time

import pyautogui
import pydirectinput 

from routines import save_routine
from pynput import keyboard 

import sys
import os

parser = argparse.ArgumentParser(description='Autobattler for FFIX.')
parser.add_argument('-m', '--manual', action='store_true', help = 'Use manual focus, use it in case of Moguri Mod')
parser.add_argument('-s', '--save', default=10, help = 'Set after how many minutes autosave the game')

args = parser.parse_args()

print(f'The game will be saved after {args.save} minutes')

encounter_rate = 2.3
enemy_per_ecounter = 2.43
save_after = 60 * int(args.save)
count = 1


#clear = lambda: os.system('clear')

if args.manual:
    print('Manual Focus Enabled, the battler will start after 5 seconds')
    time.sleep(5)
else:
    wls = pyautogui.getWindowsWithTitle("Final Fantasy IX")

    if wls == []:
        print('Game not found')
        sys.exit(0)

    print('Game found')

    w = wls[0]
    w.activate()

    print('Windows Focused')

    time.sleep(2)

print('AutoBattler Started')

pydirectinput.keyDown('right')

print(f'Battling...')

break_program = False
def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        print(' Autobattler Stopped')
        break_program = True
        return False
    
start_time = time.time()

with keyboard.Listener(on_press=on_press) as listener:
    while break_program == False:
        
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            
            measure = time.time()
            if measure - start_time > save_after:
                print(f'{args.save} minutes lapsed, activating saving routine')
                save_routine()
                start_time = time.time()

                estimate = encounter_rate * enemy_per_ecounter * count
                count = count + 1
                print(f'Estimated enemies defeated: {estimate:.2f}')

                print(f'Battling...')
    
    listener.join()

        



