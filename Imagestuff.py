from PIL import Image
import glob, os

monalisa = Image.open(r"C:\Users\joeyt_000\Desktop\monalisa.jpg")
imdata = monalisa.size
print(imdata)
inferno = Image.open(r"C:\Users\joeyt_000\Desktop\inferno.jpg")

newim = Image.blend(monalisa, inferno, .5)
newim.show()
