webbrowser.open("https://web.whatsapp.com/send?phone=+55123456789")
sleep(10)

pyautogui.typewrite("Hola estoy es un mensaje automatico")
pyautogui.press("enter")

import pyautogui, webbrowser
from time import sleep