import time, keyboard
import pyautogui as pt
from pynput.keyboard import Key, Controller

kb = Controller()

outpost = None

def locate(image):
    position = pt.locateCenterOnScreen(image, confidence=.8)
    if position is None:
        return False
    else:
        return True

def enter():
    kb.press(Key.enter)
    kb.release(Key.enter)

def down():
    kb.press(Key.down)
    kb.release(Key.down)

def quit():
    down()
    time.sleep(0.1)
    down()
    time.sleep(0.1)
    down()
    time.sleep(0.1)
    down()
    time.sleep(0.1)
    enter()
    time.sleep(0.1)
    enter()

while True:
    if locate('9.png'):
        quit()
    if locate('4.png'):
        enter()
    if locate('8.png'):
        kb.press(Key.esc)
        kb.release(Key.esc)
    if locate('5.png'):
        enter()
    if locate('1.png'):
        kb.press(Key.right)
        kb.release(Key.right)
        time.sleep(0.1)
        enter()
    if locate('2.png'):
        kb.press(Key.right)
        kb.release(Key.right)
        time.sleep(0.1)
        enter()
    if locate('3.png'):
        enter()
    if locate('6.png'):
        enter()
    if locate('7.png'):
        enter()

    



"""while True:
    if keyboard.is_pressed('p'):
        time.sleep(0.3)
        kb.press(Key.esc)
        kb.release(Key.esc)
        time.sleep(0.1)
        down()
        time.sleep(0.1)
        down()
        time.sleep(0.1)
        down()
        time.sleep(0.1)
        down()
        time.sleep(0.1)
        enter()
        time.sleep(0.1)
        enter()
        #-----------------
        time.sleep(11)
        enter()
        time.sleep(11)
        enter()
        kb.press(Key.right)
        kb.release(Key.right)
        time.sleep(0.2)
        enter()
        time.sleep(1)
        kb.press(Key.right)
        kb.release(Key.right)
        time.sleep(1.5)
        enter()
        time.sleep(0.2)
        enter()
        time.sleep(0.2)
        enter()
        time.sleep(1.5)
        enter()"""







