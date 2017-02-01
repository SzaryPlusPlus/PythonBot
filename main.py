import mouse
import ImageTests
import time

time.sleep(7)
SnakeCordX,SnakeCordY = ImageTests.FindSnake()
mouse.MovePixels(SnakeCordX,SnakeCordY)
time.sleep(3)
SnakeCordX,SnakeCordY = ImageTests.FindSnake()
mouse.MovePixels(SnakeCordX,SnakeCordY)
time.sleep(3)
SnakeCordX,SnakeCordY = ImageTests.FindSnake()
mouse.MovePixels(SnakeCordX,SnakeCordY)
time.sleep(3)
SnakeCordX,SnakeCordY = ImageTests.FindSnake()
mouse.MovePixels(SnakeCordX,SnakeCordY)