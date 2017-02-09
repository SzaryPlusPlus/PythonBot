import ImageGrab
from PIL import Image, ImageDraw
import time
import array
import os

#pxilist
#snakeColor = [255,40,0]

'''
kolor wezy
r 66 g 48 b 57
r 66 g 52 b 57
57 44 49'''
def GettingRGBSum(filename):
    im = Image.open(filename).convert('LA')
    a = im.getcolors()
    #a = a.sum()
    suma = 0 
    for pixel in a:
        suma = pixel[1][0] + suma
    print suma


    
class ImageHandling():
    AllsnakeColors = [115,0,0],[140,0,0],[123,0,0],[74,0,0]
    AllBodySnake = [51,52,47],[63,42,51],[83,64,50],[89,69,36]
    AllBodySnake2 = [107,77,49],[74,52,33],[90,60,41],[99,69,41]
    #every second pixel is the same snake y+1
    MoreThanOnepix = [115,85,57],[33,24,16],[41,28,16],[41,28,16]
    MoreThanOnepixNight = [99,85,90],[16,16,33],[49,36,49],[66,60,66]
    GreyScale = 542,607,429
    SampleImages = []
    SquareSize = 2
    ImRes = 0,0
    
       
    def __init__(self, FileToOpen):
        if(FileToOpen == ""):
            self.im = ImageGrab.grab()
        if(FileToOpen != ""):
            self.im = Image.open(FileToOpen)#.convert('LA')
        self.imPixList = self.GetImage()
        self.ImRes = self.im.size
        #print(self.ImRes)
        #print(self.imPixList[0])
    
    def GrabImage(self):
        self.im = ImageGrab.grab()
        self.imPixList = self.GetImage()
        
    def LoadSampleImages(self, Dir,PartName,SquareSize):
        print("Loading Sample Pictures...")
        self.SquareSize = SquareSize
        for root, dirs, files in os.walk(Dir):
            for file in files:            
                if PartName in file and file.endswith(".bmp"):
                     filename = os.path.join(root, file)
                     SampleIm = Image.open(filename)
                     self.SampleImages.append(SampleIm.load())
                     
    
    def CompareWithSamples(self,xcord,ycord):
        #print ("Comparing with samples: ",xcord,ycord)
        for Image in self.SampleImages:
            x = 0            
            Matching = False
            while x < self.SquareSize:
                y = 0
                while y < self.SquareSize:
                    if(x + xcord < self.ImRes[0] and y + ycord < self.ImRes[1] and Image[x,y][0] == self.imPixList[x+xcord,y+ycord][0] and Image[x,y][1] == self.imPixList[x+xcord,y+ycord][1] and Image[x,y][2] == self.imPixList[x+xcord,y+ycord][2]):
                        Matching = True
                        #print("Match at",xcord,ycord)
                    else:
                        Matching = False
                        break
                    #print(Image[x,y])
                    y = y + 1
                x = x + 1
            if Matching == True:
                print("CompareWithSamples found!")
                return True
        return False
        
    
    def GetImage(self):
        rgbList = self.im.load()
        return rgbList

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

    def HighLightOnPicture(self,cordsList):
        #y_len = len(self.imPixList)    
        #x_len = len(self.imPixList[0]) 
        
        dr = ImageDraw.Draw(self.im)
        for cord in cordsList:
            dr.rectangle(((cord[0],cord[1]),(cord[0]+2,cord[1]+2)), fill="red", outline = "blue")
        
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
        self.im.save("Found.png")
        #if not probably try
    def FindObjectInPictureMorePixes(self,ObjectToFind, first):
        print("FindObjectInPictureMorePixes...")
        found = 0
        FoundList = []
        
        x = 0
        y = 0
        #restrictions to ease looking for snakes:D to be included into objects passed
        yResWithoutBottomMenu = 420
        yResWithouthHealthBar = 25
        
        while (x < 640):
            y = yResWithouthHealthBar
            while(y < yResWithoutBottomMenu):
                colorIndex = 0
                while(colorIndex < len(ObjectToFind)):
                    #print(self.imPixList[x,y])
                    if self.imPixList[x,y][0] ==  ObjectToFind[colorIndex][0] and self.imPixList[x,y][1] ==  ObjectToFind[colorIndex][1] and self.imPixList[x,y][2] ==  ObjectToFind[colorIndex][2]:
                        if self.imPixList[x,y+1][0] ==  ObjectToFind[colorIndex+1][0] and self.imPixList[x,y+1][1] ==  ObjectToFind[colorIndex+1][1] and self.imPixList[x,y+1][2] ==  ObjectToFind[colorIndex+1][2]:
                            print("Object found at: ",x,y)
                            FoundList.append((x,y))
                            #self.HighLightOnPicture(x,y)
                            if(first):
                                print("Return!")
                                return (x,y)
                            found = 1
                    colorIndex = colorIndex + 2
                y = y + 1
            x = x + 1
        if(first):            
            return (-1,-1)
        else:
            return FoundList
    def FindObjectInPicture(self, first):
        found = 0
        FoundList = []
        
        #Lets start from the around the champ so 245, 160
        #x = 280
        #y = 170
        
        x = 280
        y = 2
        
        
        
        #restrictions to ease looking for snakes:D to be included into objects passed
        #yResWithoutBottomMenu = 420
        yResWithoutBottomMenu = 420 #LIMITED AROUND CHARACTER
        yResWithouthHealthBar = 25
        
        while (x < 640):#LIMITED AROUND CHARACTER, SHOULD BE 640
            y = yResWithouthHealthBar
            while(y < yResWithoutBottomMenu):
                if(self.CompareWithSamples(x,y)):
                    print("Found!")
                    if(first):
                        print("Return!")
                        return (x,y)
                    FoundList.append((x,y))
                y = y + 1
            x = x + 1
        if(first):            
            return (-1,-1)
        else:
            return FoundList
    def Sum(self,x,y):
        sum = 0
        while(x < x+4):
            while(y < y+4):
                #sum = self.imPixList[x,y][1] + sum
                y = y + 1
            x = x + 1
        return sum
    def FindObjectGeryScale(self,ObjectToFind, first):
        found = 0
        FoundList = []
        
        x = 0
        y = 0
        #restrictions to ease looking for snakes:D to be included into objects passed
        yResWithoutBottomMenu = 420
        yResWithouthHealthBar = 25
        
        while (x < 640):
            y = yResWithouthHealthBar
            while(y < yResWithoutBottomMenu):
                for color in ObjectToFind:
                    #print(self.imPixList[x,y][0])
                    
                    if self.Sum(x,y) == color:
                        print("Object found at: ",x,y)
                        FoundList.append((x,y))
                        #self.HighLightOnPicture(x,y)
                        if(first):
                            print("Return!")
                            return (x,y)
                        found = 1
                y = y + 1
            x = x + 1
        if(first):            
            return (-1,-1)
        else:
            return FoundList

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
        
def TestColors():
    Obraz = ImageHandling("Nemesis2.bmp")
    #print(Obraz.imPixList)
    Obraz.LoadSampleImages("SampleImgages","snake",2)
    Snakes = Obraz.FindObjectInPicture(False)
    print(Snakes)
    #print(Obraz.MoreThanOnepix)
    Obraz.HighLightOnPicture(Snakes)

#Obraz = ImageHandling("Nemesis2.bmp")
#Obraz.LoadSampleImages("SampleImgages","snake",2)

#GettingRGBSum("snake1.bmp")
#GettingRGBSum("snake2.bmp")
#TestColors()
#Obraz = ImageHandling("snakes.bmp")
#print (Obraz.imPixList[1,1])
#Obraz.FindObjectInPicture(Obraz.AllsnakeColors)
#Obraz.im.save("SnakesFound.png")
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
