# python spam_mess.py

import pyautogui as auto
import time

enter_message = input("write the message you want to spam : ")
n = int(input("Enter number of times you want to spam a message : "))
time.sleep(10)
for i in range(n):
	auto.write(enter_message)
	auto.press('enter')
completion_message = (f"spam of {n} message is successfully excecuted.Code by https://github.com/er-psycho18/er-psycho18 on github")
auto.write(completion_message)
auto.press('enter')
