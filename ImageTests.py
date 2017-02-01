import ImageGrab
from PIL import Image
import time

#pxilist
#snakeColor = [255,40,0]
AllsnakeColors = [90,69,57],[66,52,57]#,[57,44,49]
'''
kolor wezy
r 66 g 48 b 57
r 66 g 52 b 57
57 44 49'''

def GetImage():
    im = Image.open('snakes.bmp')
    #im = ImageGrab.grab()
    rgbList = im.load()

    #print rgbList[297,69]
    '''if(rgbList[1,1] == [66,16,8]):
        print("yes")
    else:
        print("no")'''
    return list(im.getdata())


def FindSnake():
    x_cord = 0
    y_cord = 0
    found = 0
    pxilist = GetImage()
    for pixel in pxilist:
        for snakeColor in AllsnakeColors:
            if pixel[0] ==  snakeColor[0] and pixel[1] ==  snakeColor[1] and pixel[2] ==  snakeColor[2]:
                print("found at: ",x_cord,y_cord)
                found = 1
                #return (x_cord,y_cord)
            if(y_cord >= 639
            ):
                x_cord = 0
                y_cord = y_cord + 1
            else:
                x_cord = x_cord + 1
    
    return (-1,-1)
FindSnake()
#time.sleep(7)
'''im = ImageGrab.grab()
rgbList = list(im.getdata())
for item in rgbList[6400]:
    print item
print (rgbList.index([255, 255, 255]))'''

#im.save('data.png', 'PNG')
#time.sleep(7)
#print("Snake at ",FindSnake())