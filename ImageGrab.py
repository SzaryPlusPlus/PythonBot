import ImageGrab
from PIL import Image, ImageDraw
import time

#pxilist
#snakeColor = [255,40,0]

'''
kolor wezy
r 66 g 48 b 57
r 66 g 52 b 57
57 44 49'''
class ImageHandling():
    AllsnakeColors = [90,69,57],[66,52,57]#,[57,44,49]
        
    def __init__(self, FileToOpen):
        if(FileToOpen == ""):
            self.im = ImageGrab.grab()
        if(FileToOpen != ""):
            self.im = Image.open(FileToOpen)
        self.imPixList = self.GetImage()
    
    def GetImage(self):
        rgbList = self.im.load()
        return list(self.im.getdata())

    def FindSnake2(self):
        x_cord = 0
        y_cord = 0
        found = 0
        
        for pixel in self.imPixList:
            for snakeColor in self.AllsnakeColors:
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

    def HighLightOnPicture(self,x,y):
        y_len = len(self.imPixList)    
        x_len = len(self.imPixList[0]) 
        
        dr = ImageDraw.Draw(self.im)
        dr.rectangle(((x,y),(x+1,y+1)), fill="red", outline = "blue")
        
        '''if(x+1 <= x_len):
            self.imPixList[x+1][y] = (255,0,0)
            if(y+1 <= y_len):
                self.imPixList[x+1][y+1] = (255,0,0)
        if(y+1 <= y_len):
            self.imPixList[x][y+1] = (255,0,0)
        if(x-1 >= 0):
            self.imPixList[x-1][y] = (255,0,0)
            if(y-1 >= 0):
                self.imPixList[x-1][y-1] = (255,0,0)
        if(y-1 >= 0):
            self.imPixList[x][y-1] = (255,0,0)'''
            
        #@TODO check if the im object is also changed when chanign pix list
        #self.im.show()
        self.im.save("at",x,"x",y,".png")
        #if not probably try
        

        '''PIL.ImageDraw.Draw.rectangle(xy, fill=None, outline=None)
        Draws a rectangle.

        Parameters:	
        xy – Four points to define the bounding box. Sequence of either [(x0, y0), (x1, y1)] or [x0, y0, x1, y1]. The second point is just outside the drawn rectangle.
        outline – Color to use for the outline.
        fill – Color to use for the fill.'''
            
    def FindObjectInPicture(self,ObjectToFind):
        found = 0
        pxilist = GetImage()
        
        x = 0
        y = 0
        #@Todo check it below
        yResWithoutBottomMenu = 440
        
        while (x < 640):
            y = 0
            while(y < ResWithoutBottomMenu):
                for color in ObjectToFind:
                    if self.imPixList[x][y] ==  color[0] and self.imPixList[x][y] ==  color[1] and self.imPixList[x][y] ==  color[2]:
                        print("Object found at: ",x,y)
                        found = 1
                y = y + 1
            x = x + 1

    def FindSnake(self):
        x_cord = 0
        y_cord = 0
        found = 0
        for pixel in self.imPixList:
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
#FindSnake()
#time.sleep(7)
'''im = ImageGrab.grab()
rgbList = list(im.getdata())
for item in rgbList[6400]:
    print item
print (rgbList.index([255, 255, 255]))'''

#im.save('data.png', 'PNG')
#time.sleep(7)
#print("Snake at ",FindSnake())
