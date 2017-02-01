import win32api, win32con, win32gui
import os
import time
import ImageGrab
import ctypes


def move(x,y):
    time.sleep(0.1)
    print("Move",x,y)
    #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/640*65535.0), int(y/480*65535.0))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x), int(y))
    
def MovePixels(x,y):
    move(-131072,-131072)
    print("MovePix",x,y)
    xpix = 131072.0 /640 # for some reason it is 65536*2
    ypix = 131072.0 /480 # for some reason it is 65536*2
    pointZero = 32768 #65536 / 2
    move(pointZero+x*xpix,pointZero+y*ypix)
    #im = ImageGrab.grab()
    #im.save(str(x)+"x"+str(y)+'.png', 'PNG')
    

