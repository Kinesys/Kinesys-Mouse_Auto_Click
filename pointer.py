import pyautogui
import time

pyautogui.PAUSE = 0.00001
pyautogui.FAILSAFE = True

x=728

y=450

for i in range(10000):
	pyautogui.click(x, y, button = 'left', clicks =1)
