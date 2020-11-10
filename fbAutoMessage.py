# Before using pyautogui you must first install the package by typing "pip install pyautogui" package in your terminal.
import pyautogui
import time

while True:
    time.sleep(0.2)
    pyautogui.typewrite("I Love You!")
    time.sleep(0.2)
    pyautogui.press('enter')