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
                     print("Loading: ",filename)
                     SampleIm = Image.open(filename)
                     self.SampleImages.append(SampleIm.load())
                     print("Loaded: ",filename)
        print("Loaded all")
    
    def LoadSampleImagesFromSprites(self, Dir,PartName,SquareSize,x,y):
        print("Loading Sample Pictures from Sprites...")
        self.SquareSize = SquareSize
        i = 0
        for root, dirs, files in os.walk(Dir):
            for file in files:            
                if PartName in file and file.endswith(".bmp"):
                     filename = os.path.join(root, file)
                     SampleIm = Image.open(filename).convert("RGB")
                     CroppedIm = SampleIm.crop((x, y, x+SquareSize, y+SquareSize))
                     CroppedIm.save("cropped\croppedNew"+str(i)+".bmp")
                     i += 1
                     self.SampleImages.append(CroppedIm.load())
        print("Finished!")
                     
    
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


    def HighLightOnPicture(self, cordsList, SquareSize):
        #y_len = len(self.imPixList)    
        #x_len = len(self.imPixList[0]) 
        
        dr = ImageDraw.Draw(self.im)
        for cord in cordsList:
            x = cord[0]
            y = cord[1]
            dr.rectangle(((x,y),(x+SquareSize,y+SquareSize)), fill="red", outline = "blue")
            #CroppedIm = self.im.crop((x, y, x+SquareSize, y+SquareSize))
            #CroppedIm.save("GeneratedSamples\\"+str(x)+"x"+str(y)+".bmp")
            
        #@TODO check if the im object is also changed when chanign pix list
        #self.im.show()
        self.im.save("Found.png")
        #if not probably try
    
    def CropFromPicture(self, cordsList, SquareSize, DestFolderName):
        #y_len = len(self.imPixList)    
        #x_len = len(self.imPixList[0]) 
        if not os.path.exists(DestFolderName):
            os.makedirs(DestFolderName)
        
        dr = ImageDraw.Draw(self.im)
        for cord in cordsList:
            x = cord[0]
            y = cord[1]
            CroppedIm = self.im.crop((x, y, x+SquareSize, y+SquareSize))
            CroppedIm.save(DestFolderName+"\\"+str(x)+"x"+str(y)+".bmp")
    
   
    def FindObjectInPicture(self, first, startX,startY):
        found = 0
        FoundList = []
        
        #Lets start from the around the champ so 245, 160
        #x = 280
        #y = 170
        
        #this does nto wrk at the moment
        x = startX
        y = startY      
        
        
        #restrictions to ease looking for snakes:D to be included into objects passed
        #yResWithoutBottomMenu = 420
        yResWithoutBottomMenu = 420 #LIMITED AROUND CHARACTER
        yResWithouthHealthBar = 25
        #lets start from where the cell left from character which should be at 280, 180
        xDefaultStart = 280
        yDefaultStart = 180
        x = xDefaultStart
        y = yDefaultStart
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
        #now lets do the rest
        x = xDefaultStart
        while (x > 0):#LIMITED AROUND CHARACTER, SHOULD BE 640
            y = yDefaultStart
            while(y > 0):
                if(self.CompareWithSamples(x,y)):
                    print("Found!")
                    if(first):
                        print("Return!")
                        return (x,y)
                    FoundList.append((x,y))
                y -= 1
            x -= 1
            
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
        
def CreateProbingCords():
    x = 289
    y = 190
    
    while(x <= 350):
        
        y = 190
        while(y <= 250):   
            TestList.append([x,y])
            y += 30
        x += 30
        
def TestColors():
    Obraz = ImageHandling("OrcPrintDay.bmp")
    #print(Obraz.imPixList)
    Obraz.LoadSampleImages("OrcsDay","",2)
    #Obraz.LoadSampleImagesFromSprites("Orc", "Orc", 2, 56, 14)
    FoundCordsList = Obraz.FindObjectInPicture(False,0,0)
    #print(Snakes)
    #print(Obraz.MoreThanOnepix)
    
    #TestList = [[289, 190], [289, 220], [289, 251], [319, 250], [349, 190], [349, 220], [349, 250]]
    #print(TestList)
    Obraz.HighLightOnPicture(FoundCordsList,2)

#TestColors()

#Obraz = ImageHandling("OrcPrintNight.bmp")
#Obraz.LoadSampleImages("SampleImgages","snake",2)
#TestList = [[289, 190], [289, 220], [289, 247], [349, 190], [349, 220], [349, 237], [320, 215], [350, 157]]
#Obraz.HighLightOnPicture(TestList,2)
#Obraz.CropFromPicture(TestList,2,"OrcsNight")
#Obraz.LoadSampleImagesFromSprites("Orc","Orc",2)
#Obraz.LoadSampleImages("Orc","cropped",2)
'''for Image in Obraz.SampleImages:
    print (Image[0,0])
    print (Image[1,0])
    print (Image[0,1])
    print (Image[1,1])'''

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
