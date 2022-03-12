import time 
import threading 
from pynput.mouse import Button, Controller 
from pynput.keyboard import Listener, KeyCode 

from playsound import playsound

delay = 5.000
button = Button.left 
start_stop_key = KeyCode(char='`') 
stop_key = KeyCode(char='`') 

class ClickMouse(threading.Thread): 
	def __init__(self, delay, button): 
		super(ClickMouse, self).__init__() 
		self.delay = delay 
		self.button = button 
		self.running = False
		self.program_running = True

	def start_clicking(self): 
		self.running = True

	def stop_clicking(self): 
		self.running = False

	def exit(self): 
		self.stop_clicking() 
	
	def run(self): 
		while self.program_running: 
			while self.running: 
				mouse.click(self.button) 
				time.sleep(self.delay) 
			time.sleep(0.1) 


mouse = Controller() 
click_thread = ClickMouse(delay, button) 
click_thread.start() 

def start():
    mouse = Controller() 
    click_thread = ClickMouse(delay, button) 
    click_thread.start()

print("ClickMouse created")
def on_press(key): 
	if key == start_stop_key: 
		if click_thread.running: 
			playsound('clock.mp3')
			click_thread.stop_clicking() 
		else: 
			playsound('click.mp3')
			click_thread.start_clicking() 
	elif key == stop_key: 
		click_thread.exit() 

with Listener(on_press=on_press) as listener: 
	listener.join() 
