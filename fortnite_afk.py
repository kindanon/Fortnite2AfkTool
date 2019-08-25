from pynput.mouse import Button, Controller as m_cont
from pynput.keyboard import Key, Controller as k_cont
from PIL import ImageGrab, Image
import time

mouse = m_cont()
keyboard = k_cont()
hc = (1600,950)
bc = (1635,325)
ec = (235,95)
ic = (476,882)
mc = (615,882)
sc = (500,755)

while True:
	#start infinite loop
	time.sleep(3)
	
	#hide from afk timer
	keyboard.press(Key.ctrl)
	time.sleep(.5)
	keyboard.release(Key.ctrl)
	
	#take screenshot	
	img = ImageGrab.grab(bbox = (0,0,1920,1080))
	
	#get pixels from image
	home = img.getpixel(hc)
	bus = img.getpixel(bc)
	end = img.getpixel(ec)
	item = img.getpixel(ic)
	items = img.getpixel(mc)
	survey = img.getpixel(sc)
	
	#if on home
	if home == (245,  231, 72):
		mouse.position = hc
		mouse.click(Button.left, 1)
		time.sleep(.5)
		mouse.position = (0,0)
	
	#if end game
	elif end == (255,  0, 22):
		mouse.position = (1820,1050)
		mouse.click(Button.left, 1)	
		time.sleep(.5)
		mouse.position = (0,0)
	
	#if items
	elif item == (255,  255, 255):
		mouse.position = ic
		mouse.click(Button.left, 1)	
		time.sleep(.5)
		mouse.position = (0,0)
		
	elif items == (255,  255, 255):
		mouse.position = mc
		mouse.click(Button.left, 1)	
		time.sleep(.5)
		mouse.position = (0,0)	
	
	#if survey
	elif survey == (157,195,255):
		mouse.position = sc
		mouse.click(Button.left, 1)	
		time.sleep(.5)
		mouse.position = (0,0)
	#if on bus
	elif bus == (101,  159, 55):
		time.sleep(20)
		keyboard.press(' ')
		time.sleep(.5)
		keyboard.release(' ') 
		time.sleep(.5)
		keyboard.press(' ')
		time.sleep(.5)
		keyboard.release(' ') 
		time.sleep(120)	 