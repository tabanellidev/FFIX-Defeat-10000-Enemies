import pyautogui
import pydirectinput
import time

def encounter_cheat():
    pydirectinput.press('backspace')
    time.sleep(1.5)
    pydirectinput.press('j')
    time.sleep(1.5)
    pydirectinput.press('backspace')

def save_routine():

    print('Save routine activated')

    pydirectinput.keyUp('right')

    print('Cleanin post-battle screen')
    #Clean up post-battle screen
    for i in range(1,30):
        pydirectinput.press('x')

    pydirectinput.keyUp('right')

    #Activate cheats
    encounter_cheat()
    
    print('Encounter disabled')

    for i in range(1,6):
        pydirectinput.press('up')

    for i in range(1,7):
        pydirectinput.press('right')

    #Change room
    pydirectinput.press('up')
    time.sleep(1.5)
    pydirectinput.press('down')

    for i in range(1,6):
        pydirectinput.press('down')
    
    #Disable cheats
    encounter_cheat()
    print('Encounter enabled')

    pydirectinput.keyDown('right')
