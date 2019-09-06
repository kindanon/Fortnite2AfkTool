from pynput.mouse import Button, Controller as m_cont
from pynput.keyboard import Key, Controller as k_cont
from PIL import ImageGrab, Image
import time

mouse = m_cont()
keyboard = k_cont()

hc = (1600,950)
bc = (1675,335)
ec = (235,95)
mc = (615,882)
ic = (476,882)
sc = (500,755)
nc = (655, 940)

new_items = (750,950)
new_item = (540,950)
new_news = (680,950)
new_spec = (580,950)
new_exit = (1820,1050)
while True:
	
	time.sleep(5) #start infinite loop
		
	img = ImageGrab.grab(bbox = (0,0,1920,1080)) #take screenshot
	
	#get pixels from image
	home = img.getpixel(hc)
	bus = img.getpixel(bc)
	
	#if on home
	if home == (245,  232, 72):
		mouse.position = hc
		mouse.click(Button.left, 1)
		time.sleep(.5)
		mouse.position = (0,0)

	#if on bus
	elif bus == (101,  159, 55):
		time.sleep(12)
		keyboard.press(' ')
		time.sleep(.5)
		keyboard.release(' ') 
		time.sleep(.5)
		keyboard.press(' ')
		time.sleep(.5)
		keyboard.release(' ') 
		time.sleep(120)	
		
	#just spam click bro	
	mouse.position = new_items
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = new_item
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = new_news
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = new_spec
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = new_exit
	mouse.click(Button.left, 1)
	time.sleep(.1)
	"""
	mouse.position = ec
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = mc
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = ic
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = sc
	mouse.click(Button.left, 1)
	time.sleep(.1)
	mouse.position = nc
	mouse.click(Button.left, 1)
	time.sleep(.1)
	"""