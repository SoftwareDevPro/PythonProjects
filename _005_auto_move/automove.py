
import pyautogui, time, random

while True:
    x = round(2 * random.random() - 1) * 5 # -5, 0 5
    y = round(2 * random.random() - 1) * 5 # -5, 0 5
    pyautogui.moveRel(x, y)
    time.sleep(2)
