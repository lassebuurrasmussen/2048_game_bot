import pyautogui
import time

for i in list(range(3))[::-1]:
    print(i + 1)
    time.sleep(1)

pause_between = 0.2

while True:
    print('right')
    pyautogui.keyDown('right')
    pyautogui.keyUp('right', pause=pause_between)

    print('left')
    pyautogui.keyDown('left')
    pyautogui.keyUp('left', pause=pause_between)

    print('down')
    pyautogui.keyDown('down')
    pyautogui.keyUp('down', pause=pause_between)

    print('up')
    pyautogui.keyDown('up')
    pyautogui.keyUp('up', pause=pause_between)
