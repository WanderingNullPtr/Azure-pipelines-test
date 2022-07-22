from PIL import ImageGrab
import sys
import time

time.sleep(5)
GameWindow = ImageGrab.grab( bbox = (int(sys.argv[2]),int(sys.argv[3]),
                            int(sys.argv[4]),int(sys.argv[5])) )
GameWindow.save(sys.argv[1])