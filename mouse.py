import win32api, win32con
import os
import time

# Globals
# ------------------
 
x_offset = 0
y_offset = 0

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left Down'
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left release'
    
def mousePos(cord):
    win32api.SetCursorPos((x_offset + cord[0], y_offset + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_offset
    y = y - y_offset
    print x,y

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."          #completely optional. But nice for debugging purposes.
    
def startGame():
    #location of first menu
    mousePos((182, 225))
    leftClick()
    time.sleep(.1)
     
    #location of second menu
    mousePos((193, 410))
    leftClick()
    time.sleep(.1)
     
    #location of third menu
    mousePos((435, 470))
    leftClick()
    time.sleep(.1)
     
    #location of fourth menu
    mousePos((167, 403))
    leftClick()
    time.sleep(.1)

#startGame()
time.sleep(10)
mousePos((320, 240))
leftClick()
print(win32api.GetCursorPos())
