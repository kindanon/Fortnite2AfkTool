import win32gui
import win32api
import win32con
import time
from PIL import ImageGrab, Image

hwnd = win32gui.FindWindow("UnrealWindow", None) #find by class

#RGB CONSTANTS
#-------------
bus_rgb = (101,159,55)
#-------------

while(1):
    time.sleep(1) #wait for loop

    #get window location + frame
    coords = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox = (coords[0],coords[1],coords[2],coords[3]))
    #--------------

    #location setup
    bus_coords = (int((coords[2]*.50668)), int((coords[3]*.19730)))
    playParam  = win32api.MAKELONG(int(((coords[2]-coords[0])*.89516)), int((coords[3]-coords[1])*.61671))
    readyParam = win32api.MAKELONG(int(((coords[2]-coords[0])*.87844)), int((coords[3]-coords[1])*.63763))
    fillParam  = win32api.MAKELONG(int(((coords[2]-coords[0])*.83075)), int((coords[3]-coords[1])*.63108))
    tabinParam = win32api.MAKELONG(int(((coords[2]-coords[0])*.5)), int((coords[3]-coords[1])*.5))
    #--------------

    #simulate click for tab in 
    #win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tabinParam)
    #time.sleep(.1)
    #win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, tabinParam)
    #--------------

    #bus actions
    if (bus_rgb == img.getpixel(bus_coords)):
        time.sleep(12)
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        time.sleep(.1)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)
        time.sleep(.1)
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
        time.sleep(.1)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)
        time.sleep(120)
    #--------------

    #mouse click function
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, fillParam)
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_LBUTTON, 0)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, fillParam)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_LBUTTON, 0)
    #--------------

#old info
#find by name
#print(win32gui.FindWindow(None, "Fortnite"))

#iterate to find information
#def enumHandler(hwnd, lParam):
#    if "Fortnite" in win32gui.GetWindowText(hwnd):
#        print(str(win32gui.GetWindowText(hwnd)))
#        print(str(win32gui.GetClassName(hwnd)))
#win32gui.EnumWindows(enumHandler, None)

#coords[0] = x
#coords[1] = y
#coords[2] = width
#coords[3] = height
