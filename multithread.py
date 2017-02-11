import mouse
import ImageHandling as Img
import time
import threading
import Queue
import signal
import sys

exitFlag = 0

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        global exitFlag
        exitFlag = 1
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
#signal.pause()

print("Started sleeping...")
time.sleep(8)
print("Testing!")

Obraz = Img.ImageHandling("")
Obraz.LoadSampleImages("SnakesDay","",2)

def TestSnakeHit(): 
    print("Grabbing image")
    Obraz.GrabImage()
    print("FindObjectInPicture")
    x,y = Obraz.FindObjectInPicture(True,0,0)#270,160)
    print("return")
    return(x,y)
        
def TestMouseMove():
    repeat = 0 
    while(repeat < 20):
        mouse.MoveOneRight()
        mouse.MoveOneRight()
        mouse.MoveOneLeft()
        mouse.MoveOneLeft()
        repeat = repeat+1
#TestSnakeHit()

# Create new threads
class SnakesThread (threading.Thread):
    def __init__(self, threadID, name, counter,queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
    def run(self):
        global queueLock
        print "Starting " + self.name
        while(self.counter > 0):
            if(exitFlag):
                break
            xy = TestSnakeHit()
            #print("acquire lock from imthread")
            queueLock.acquire()
            self.queue.put(xy)
            queueLock.release()
            #print("released lock from imthread")
            self.counter -= 1
        print "Exiting " + self.name
        
# Create new threads
class printThread (threading.Thread):
    def __init__(self, threadID, name, counter,queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
    def run(self):
        print "Starting " + self.name
        global queueLock
        while(self.counter > 0):
            #print("acquire lock from printThread")
            #queueLock.acquire()
            if(exitFlag):
                break
                
            x,y = self.queue.get()
            if(x > 0):
                mouse.MovePixels(x,y)
                #check if you are not clicking on a character then do lef click
                if(x>307 and x<332 and y>175 and y<205):
                    mouse.LeftClick(0.4)
                else:                
                    mouse.RightClick(0.4)
                #move it back so it does  not cover
                mouse.MovePixels(0,0)
            self.counter -= 1
        print "Exiting " + self.name
        
# Create new threads
queueLock = threading.Lock()
workQueue = Queue.Queue(1)

thread1 = SnakesThread(1, "SnakesThread\n", 1000,workQueue)
thread2 = printThread(2, "printThread\n", 1000,workQueue)

# Start new Threads
thread1.start()
#time.sleep(5)
thread2.start()

#empty loop
print("main idle")
time.sleep(10*60)
print("EXITING @#@$$%#$%#$%#$%#$%#$%#$%#$%#$%")

thread1.exit()
thread2.exit()

#thread1.join()
#thread2.join()
    
############# NOTES@@@@@@@@@@@@@@@@@
# Find the snakes in relative position to you and then move and chek again start hittinh




#MovePixels
#press()