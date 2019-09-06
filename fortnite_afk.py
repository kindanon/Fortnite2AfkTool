from pynput.mouse import Button, Controller as m_cont
from pynput.keyboard import Key, Controller as k_cont
from PIL import ImageGrab, Image
import time

mouse = m_cont()
keyboard = k_cont()

#coordinates of buttons / icons
c_start = (1600,950)
c_bus = (1635,325)
c_dead = (235,95)
c_escape = (1820,1050)
c_survey = (500,755)
c_news = (655, 940)
c_item = (476,882)
c_items = (615,882)
c_list = [c_start, c_bus, c_dead, c_escape, c_survey, \
c_news, c_item, c_items]

#color of button / icons
rgb_start = (245,  232, 72)
rgb_bus = (101,  159, 55)
rgb_dead = (255,  0, 22)
rgb_escape = None
rgb_survey = (157,195,255)
rgb_news = (255,255,255)
rgb_item = (255,  255, 255)
rgb_items = (255,  255, 255)
rgb_list = [rgb_start, rgb_bus, rgb_dead, rgb_escape, rgb_survey, \
rgb_news, rgb_item, rgb_items]

img = ImageGrab.grab(bbox = (0,0,1920,1080))

for i_coord, coord in enumerate(c_list):
	pixel = img.getpixel(coord)
	
	for i_rgb, rgb in enumerate(rgb_list):
		if pixel == rgb
			actions(i_rgb)

			
def actions(case):
	switcher = {
		0: start,
		1: bus,
		2: dead,
		3: escape,
		4: survey,
		5: news,
		6: item,
		7: items,
	}
	func = switcher.get(i)
	return func()


hc = (1600,950)
bc = (1635,325)
ec = (235,95)
ic = (476,882)
mc = (615,882)
sc = (500,755)
nc = (655, 940)
	
while True:
	
	#mouse.position = hc
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
	news = img.getpixel(nc)
	
	#if on home
	if home == (245,  232, 72):
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
	
	#if news
	elif news == (255,255,255):
		mouse.position = nc
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