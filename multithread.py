import mouse
import ImageHandling as Img
import time
import threading
import Queue

print("Started sleeping...")
time.sleep(1)
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
    Obraz.LoadSampleImages("SamplesNight","snake",2)
    print("Looking for snakes!...")
    print(time.ctime(time.time()))
    time.sleep(0.01)
    print("GrabImage...")
    Obraz.GrabImage()
    #print (Obraz.imPixList[1,1])
    print("FindObjectInPicture...")
    x,y = Obraz.FindObjectInPicture(True)
    print("return...")
    time.ctime(time.time())
    return(x,y)
    '''if(x != -1):
        mouse.MovePixels(x,y)
        mouse.RightClick(0.3)
        #move it back so it does  not cover
        mouse.MovePixels(0,0)'''
        
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
class imthread (threading.Thread):
    def __init__(self, threadID, name, counter,queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
    def run(self):
        print "Starting " + self.name
        while(self.counter > 0):
            xy = TestSnakeHit()
            print("acquire lock from imthread")
            queueLock.acquire()
            self.queue.put(xy)
            queueLock.release()
            print("released lock from imthread")
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
        while(self.counter > 0):
            print("acquire lock from printThread")
            queueLock.acquire()
            if not workQueue.empty():
                print(self.queue.get())
                queueLock.release()
            else:
                print("empty")
                queueLock.release()
                time.sleep(1)
            print("released lock from printThread")
            self.counter -= 1
        print "Exiting " + self.name
        
# Create new threads
queueLock = threading.Lock()
workQueue = Queue.Queue(10)

thread1 = imthread(1, "ImageThread\n", 10,workQueue)
thread2 = printThread(2, "Thread-2\n", 10,workQueue)

# Start new Threads
thread1.start()
time.sleep(5)
thread2.start()

#empty loop
print("main idle")
time.sleep(10)

thread1.join()
thread2.join()
    
############# NOTES@@@@@@@@@@@@@@@@@
# Find the snakes in relative position to you and then move and chek again start hittinh




#MovePixels
#press()