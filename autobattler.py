import pyautogui
import pydirectinput
import time

print('AutoBattler Started')

w = pyautogui.getWindowsWithTitle("Final Fantasy IX")[0]
w.activate()

max = 100000

for i in range(1,max):

    print(f'{i}/{max}')

    pydirectinput.keyDown('right')

    pydirectinput.press('x')
    pydirectinput.press('x')
    pydirectinput.press('x')
    


print('AutoBattler Stopped')