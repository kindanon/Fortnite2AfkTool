from pynput.mouse import Button, Controller as m_cont
from pynput.keyboard import Key, Controller as k_cont
from PIL import ImageGrab, Image
import time

mouse = m_cont()
keyboard = k_cont()
hc = (1600,950)
bc = (1640,325)
ec = (1754,1038)

while True:
	#start infinite loop
	time.sleep(1)
	
	#take screenshot	
	img = ImageGrab.grab(bbox = None)
	
	#get pixels from image
	home = img.getpixel(hc)
	bus = img.getpixel(bc)
	end = img.getpixel(ec)
	
	#if on home
	if home == (245,  231, 72):
		mouse.position = hc
		mouse.click(Button.left, 1)
		time.sleep(.5)
		mouse.position = (0,0)
		time.sleep(15)
		
	
	#if on bus
	elif bus == (0,  211, 246):
		keyboard.press(' ')
		time.sleep(30)
	
	#if end game
	elif end == (137,  138, 146):
		mouse.position = ec
		mouse.click(Button.left, 1)		