import ImageGrab
from PIL import Image
import time


im = Image.open('data.bmp')
rgbList = im.load()

print rgbList[297,69]
if(rgbList[1,1] == [66,16,8]):
    print("yes")
else:
    print("no")
pxilist = list(im.getdata())

#pxilist
snakeColor = [255,40,0]

x_cord = 0
y_cord = 0
for pixel in pxilist:
    if pixel[0] ==  snakeColor[0] and pixel[1] ==  snakeColor[1] and pixel[2] ==  snakeColor[2]:
        print("found at: ",x_cord,y_cord)
    if(x_cord >= 639):
        x_cord = 0
        y_cord = y_cord + 1
    else:
        x_cord = x_cord + 1
 
#time.sleep(7)
'''im = ImageGrab.grab()
rgbList = list(im.getdata())
for item in rgbList[6400]:
    print item
print (rgbList.index([255, 255, 255]))'''

#im.save('data.png', 'PNG')