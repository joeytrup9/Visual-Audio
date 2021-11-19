from tkinter.constants import X
from graphics import *
import random
from PIL import Image

image = Image.open(r"C:\Users\joeyt_000\Desktop\monalisa.jpg")
#image.show()
imdata = image.size
print(imdata)
WIDTH = imdata[1]
HEIGHT = imdata[0]
win = GraphWin(width = WIDTH, height = HEIGHT)
#win.setBackground("black")
pt = Point(250,250)
#pt.draw(win)
circle = Circle(pt, 20)
arr = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]
random.seed(53475078)
#rand = random.randrange(0, 500)
#print(rand)
for i in range(HEIGHT):
    for j in range(WIDTH):
        arr[j][i] = Point(j,i)
        #if i % 5 == 0 and j % 5 == 0:
        #    arr[j][i].draw(win)
#rand = random.randrange(0, 500)
#rand2 = random.randrange(0,500)

activated_pixels = [arr[250][250]]

while 1:
    for x in activated_pixels:
        activated_pixels.append()
    
    

win.getMouse()

def getPixelCoordinates(Point):
    for x in arr:
        for y in arr[x]:
            if