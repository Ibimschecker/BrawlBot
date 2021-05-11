import pyautogui
import numpy as np
import time
import cv2

# possible moves
moves = [
    'left', 'up', 'right', 'down', 'z', 'x', 'c',
    'left z', 'up z', 'right z', 'down z',
    'left x', 'up x', 'right x', 'down x',
    'left c', 'up c', 'right c', 'down c',
]

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "recording.avi"
fps = 10.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

pyautogui.getWindowsWithTitle('Brawlhalla')[0].maximize()
pyautogui.getWindowsWithTitle('PyCharm')[0].minimize()

time.sleep(1)

duration = 10  # recording lasting for ... seconds
start = time.time()

while time.time() - start < duration:
    time.sleep(.5)
    move = np.random.choice(moves).split()  # select move at random
    print(move)

    if move[0] == 'left' or move[0] == 'right' or move[0] == 'up' or move[0] == 'down':
        if len(move) > 1:
            pyautogui.keyDown(move[0])
            pyautogui.press(move[1])
            pyautogui.keyUp(move[0])
        else:
            pyautogui.keyDown(move[0])
            time.sleep(.5)
            pyautogui.keyUp(move[0])
    else:
        pyautogui.press(move[0])

    img = pyautogui.screenshot()

    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    # TODO: stop if screen is paused or platform isn't showing

out.release()
