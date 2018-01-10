# Twitter-Image-Processor
Connecting to a twitter account with public and private keys. The tweepy library allows the user to send out tweet on a timer or when a function is called. The purpose of this bot was to inverse the colors of images that are DM'd to the account and tweet them out again. The bot can also find images in http code through a quick webscrape
```python
  #The url is from the selenium bot, this will return the url for beautiful soup
def searchForImage(url,tw):
	images = list()
	base = u.urlopen(url).read()
	soup = BeautifulSoup(base,'html.parser')
	div = soup.find_all('img')
	for image in div:
		 if '.jpg' in image['src']:
		 	images.append(image['src'])

	randImageURL = random.choice(images)
	u.urlretrieve(url,'pic.jpg')
```
# Image Portion
When these functions are called, there is a new image canvas that is created
```python
#Create a new Image based on the properites of the input image
def configDraw(image):
	im = Image.open(image)
	global newIm
	newIm = Image.new('RGBA',im.size,color=(255,255,255))
	global font
	font = ImageFont.truetype('C:\Windows\Fonts\Arial',3,0,'unic')
	global draw
	draw = ImageDraw.Draw(newIm,mode='RGBA')
```
*Image pixels are now loaded into a tuple array.*
```python
#Returns a tuple matrix of all image pixels in the image
def imagePixels(image):
	pixels = list()
	im = Image.open(image)
	width,height = im.size
	pix = im.load()
	pixels.append(pix)
	return pixels,width,height
```
With the new list of pixels. The brightness of the pixel is then calculated. Based on the brightness of the image, a pixel is either turned to a black color or a white color.
```python
#Converts each pixel in the matrix to a inverse color hue
def changeBW(pixels,width,height):
	for i in range(len(pixels)):
		for x in range(width):
			for y in range(height):
				calcBrightnessToBinary(pixels[i][x,y],x,y)			#This function will be inversing the color scheme of the image
	newIm.show()
```
```python
#Checks the brightness of the pixels and decides weather to change the pixel to black or white
def calcBrightnessToBinary(pixel,x,y):
	#If the brightness is above 127, then 1, else 0
	avg = (pixel[0] + pixel[1] + pixel[2])/3
	if avg > 127:
		draw.text((x,y),'1',fill=(0,0,0),font=font,anchor=None)
		#You will draw here
	else:
		draw.text((x,y),'0',fill=(0,0,0),font=font,anchor=None)
		#replace the pixel here as well???
```
*Example*
![BEFORE](https://i.gyazo.com/df554584f4d087e98ffccd3f17bbc3da.jpg)
*After Processing*
![AFTER](https://i.gyazo.com/da395cf769281bedccc76bab110ce306.png)

# Limitations
One of the main reasons why I did not continue with this project is because the image processing was way too time expensive..
