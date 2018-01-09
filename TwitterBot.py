import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import tweepy
import urllib as u
import random
import threading
from ImageProcess import imagePixels as p
from ImageProcess import changeBW as c
from ImageProcess import configDraw as conf

def Twitter():
	conKey='2Zgh88DTff7ZUCclSmL2aVrMI'
	conSec='4p3nJ7W1vpUWEJKaR2feOD9lT9LJpBNY4Ef2PjdljsNTVoZRtK'
	accKey='3016876398-0xq0kYB3JTUAUekx4MJco1s19rjceK0OEa76DrJ'
	accSec='Tn9TysWSiW3zpoUrSX8Y2dQlnHphQGOvVVDtxTpPuX0UK'
	auth = tweepy.OAuthHandler(conKey,conSec)
	auth.set_access_token(accKey,accSec)
	tw = tweepy.API(auth)
	return tw


def destroyMessages(tw):
	mesg = tw.direct_messages(full_text=True)
	for i in mesg:
		tw.destroy_direct_message(i.id)
		print 'gone'

def sendHint(tw):
	#Send a tweet out
	tw.update_status(status=' ^.^, soon im still in dev...')
	print 'sent!!'



#This is getting the dm messages, This will then activate the selenium bot and then return a url
def findDM(tw):
	mesg = tw.direct_messages(full_text=True)
	for dm in mesg:
		line = dm.text
		if len(line.split()) == 1 and '/' not in line:
			url = webDriver(line)
			tw.destroy_direct_message(dm.id)
			return url
		elif len(mesg) is not 0 and len(line.split()) > 1:
			print 'wrong'


#This is the selenium bot, that will search the image website, this will show the url
#This is to webcrawl over chrome
#Selenium is used for this instance
def webDriver(imageName):
	driver = webdriver.Chrome(executable_path='/Users/jameslemieux/Desktop/chromedriver')
	driver.get('https://pixabay.com/')
	elem = driver.find_element_by_id('id_q')
	elem.clear()
	elem.send_keys(imageName)
	elem.send_keys(Keys.RETURN)
	return driver.current_url


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


def sendImageToTwitter(file,tw):
	#Alright we ready to send
	tw.update_status_with_media(filename=file)

#The image processing portion
conf('puppy.jpg')
pixels,width,height = p('puppy.jpg')
c(pixels,width,height)
