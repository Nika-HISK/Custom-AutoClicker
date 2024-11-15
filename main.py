import keyboard
import mouse
import time

isClickable = False

def set_clicker():
    global isClickable
    if isClickable:
        isClickable = False
        print("off")
    else:
        isClickable = True
        print("on")  

keyboard.add_hotkey("Alt + T", set_clicker)

while True:
    if isClickable:
        mouse.double_click(button="left")
        time.sleep(0.01)
