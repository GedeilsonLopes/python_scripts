from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(659, 500) [0] == 0:
        click(659, 500)
    if pyautogui.pixel(755, 500) [0] == 0:
        click(755, 500)
    if pyautogui.pixel(829, 500) [0] == 0:
        click(829, 500)
    if pyautogui.pixel(931, 500) [0] == 0:
        click(931, 500)