

webbrowser.open("https://web.whatsapp.com/send?phone=+55123456789")
sleep(10)

with open ("spam.txt", "r") as file:
for line in file:
pyautogui.typewrite(line)
pyautogui.press("enter")

import pyautogui, webbrowser
from time import sleep