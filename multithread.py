import mouse
import ImageHandling as Img
import time
import threading
import Queue

print("Started sleeping...")
time.sleep(8)
print("Testing!")

Obraz = Img.ImageHandling("")
Obraz.LoadSampleImages("GeneratedSamples","",2)

def TestSnakeHit(): 
    print("Grabbing image")
    Obraz.GrabImage()
    print("FindObjectInPicture")
    x,y = Obraz.FindObjectInPicture(True)
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
            queueLock.acquire()
            if not workQueue.empty():
                x,y = self.queue.get()
                if(x > 0):
                    mouse.MovePixels(x,y)
                    mouse.RightClick(0.5)
                    #move it back so it does  not cover
                    mouse.MovePixels(0,0)
                queueLock.release()
            else:
                print("empty")
                queueLock.release()
                time.sleep(0.1)
            #print("released lock from printThread")
            self.counter -= 1
        print "Exiting " + self.name
        
# Create new threads
queueLock = threading.Lock()
workQueue = Queue.Queue(3)

thread1 = SnakesThread(1, "SnakesThread\n", 1000,workQueue)
thread2 = printThread(2, "printThread\n", 1000,workQueue)

# Start new Threads
thread1.start()
#time.sleep(5)
thread2.start()

#empty loop
print("main idle")
time.sleep(60)

thread1.join()
thread2.join()
    
############# NOTES@@@@@@@@@@@@@@@@@
# Find the snakes in relative position to you and then move and chek again start hittinh




#MovePixels
#press()