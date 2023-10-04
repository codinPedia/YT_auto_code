import time
import random
import keyboard
from pynput.keyboard import Controller

running = True
keyboard_controller = Controller()


with open('files/text.txt') as f: TEXT = f.read()



def write(text):
	chars = list(text)

	for char in chars:
		keyboard_controller.type(char)
		time.sleep(random.uniform(0, 0.2))


def end():
	global running
	running = False

keyboard.add_hotkey('ctrl+shift+1', lambda: write(TEXT))
keyboard.add_hotkey('Ctrl+Shift+0', end)

# Keep running
while running: time.sleep(1)
