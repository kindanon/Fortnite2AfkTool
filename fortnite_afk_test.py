from pynput.mouse import Button, Controller as m_cont
from pynput.keyboard import Key, Controller as k_cont

import cv2  
import numpy

from PIL import ImageGrab, Image
import time

mouse = m_cont()
keyboard = k_cont()

playi = cv2.imread("fnt_play.png")
busi = cv2.imread("fnt_drop.png")
exiti = cv2.imread("fnt_leave.png")


def main():
#	load_assets()
	home()
	#TODO
	
	
def scanner(template):
	scr_img = scr_cap()
	cv_img = cv_pil(scr_img)
	scan(cv_img, template)
	
def scr_cap():
	return ImageGrab.grab(bbox = None)

def cv_pil(scr_img):
	cv_img = numpy.array(scr_img)
	return cv_img[:, :, ::-1].copy() 	
	
def scan(cv_img, template):
	result = cv2.matchTemplate(cv_img,template,cv2.TM_SQDIFF_NORMED) 
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	
	if numpy.subtract((max_loc),(min_loc)) is None:
		
		print("i am none\n")
		
		return (0,0)
	else:
		
		print(numpy.subtract((max_loc),(min_loc)))
		
		return numpy.subtract((max_loc),(min_loc))
	
def sleep(i):
	time.sleep(i)

#def load_assets():
#	playi = cv2.imread("fnt_play.png")
#	busi = cv2.imread("fnt_drop.png")
#	exiti = cv2.imread("fnt_leave.png")
	


def home():
	xy = scanner(playi)
	if xy != (0,0):
		mouse.position = xy
		mouse.click(Button.left, 1)
	sleep(2)
	home()
	
	
def bus():
	xy = scanner(busi)
	keyboard.press(' ')
	keyboard.re(' ')
	sleep(3)
	
def exit():
	xy = scanner(exiti)
	mouse.position = xy
	mouse.click(Button.left, 1)	
	
def item():
	item()
	#TODO
	
	
	
if __name__ == "__main__":
	main()