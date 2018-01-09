#Here I wanted to add some extra things for my bot, this is so it makes it look a lot more clean
from matplotlib.pyplot import imread
import numpy as np
from PIL import Image,ImageDraw,ImageFont



#Create a new Image based on the properites of the input image
def configDraw(image):
	im = Image.open(image)
	global newIm
	newIm = Image.new('RGBA',im.size,color=(255,255,255))
	global font
	font = ImageFont.truetype('C:\Windows\Fonts\Arial',3,0,'unic')
	global draw
	draw = ImageDraw.Draw(newIm,mode='RGBA')

#Returns a tuple matrix of all image pixels in the image
def imagePixels(image):
	pixels = list()
	im = Image.open(image)
	width,height = im.size
	pix = im.load()
	pixels.append(pix)
	return pixels,width,height

#Converts each pixel in the matrix to a inverse color hue
def changeBW(pixels,width,height):
	for i in range(len(pixels)):
		for x in range(width):
			for y in range(height):
				calcBrightnessToBinary(pixels[i][x,y],x,y)			#This function will be inversing the color scheme of the image
	newIm.show()

#Checks the brightness of the pixels and decides weather to change the pixel to black or white
def calcBrightnessToBinary(pixel,x,y):
	#If the brightness is above 127, then 1, else 0
	avg = (pixel[0] + pixel[1] + pixel[2])/3
	if avg > 127:
		draw.text((x,y),'1',fill=(0,0,0),font=font,anchor=None)
		#You will draw here
	else:
		draw.text((x,y),'0',fill=(0,0,0),font=font,anchor=None)
		#replce the pixel here as well, idk how but we will learn!
