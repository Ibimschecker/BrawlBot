import pyautogui
import numpy as np
import time
# possible moves
moves = [
    'left', 'up', 'right', 'down', 'z', 'x', 'c'
]


def run():
    while True:
        pyautogui.press(moves[np.random.randint(0, len(moves))])
        time.sleep(.3)


time.sleep(5)
run()
