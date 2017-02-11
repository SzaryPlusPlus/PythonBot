import mouse
import ImageHandling as Img
import time

print("Started sleeping...")
time.sleep(8)
print("Testing!")
def TestSnakeHit():
    i = 0
    '''while(i < 10000):
        time.sleep(0.01)
        Obraz = Img.ImageHandling("")
        #print (Obraz.imPixList[1,1])
        x,y = Obraz.FindObjectInPicture(Obraz.AllBodySnake2, True)
        if(x != -1):
            mouse.MovePixels(x,y)
            mouse.Press(0.1)
        i = i + 1'''
    Obraz = Img.ImageHandling("")
    Obraz.LoadSampleImages("GeneratedSamples","",2)
    while(i < 10000):
        print("Looking for snakes!...")
        time.sleep(0.01)
        Obraz.GrabImage()
        #print (Obraz.imPixList[1,1])
        x,y = Obraz.FindObjectInPicture(True)
        if(x != -1):
            mouse.MovePixels(x,y)
            mouse.RightClick(0.3)
            #move it back so it does  not cover
            mouse.MovePixels(0,0)
        i = i + 1
def TestMouseMove():
    repeat = 0 
    while(repeat < 20):
        mouse.MoveOneRight()
        mouse.MoveOneRight()
        mouse.MoveOneLeft()
        mouse.MoveOneLeft()
        repeat = repeat+1
TestSnakeHit()
    
############# NOTES@@@@@@@@@@@@@@@@@
# Find the snakes in relative position to you and then move and chek again start hittinh




#MovePixels
#press()