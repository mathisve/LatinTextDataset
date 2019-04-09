#Mathis Van Eetvelde 2019
#refer to LICENSE.md for copyright and licensing info

import json
import sys
import os
from tqdm import tqdm

import subprocess

from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver.ChromeDriverVersion


class main(object):
	def __init__(self):
		self.checkIfFileExists()
		self.websites = json.load(open('websites.json'))

		try:
			self.chrome_options = webdriver.ChromeOptions()
			print(sys.argv[1].lower)
			if(sys.argv[1].lower() in ["-v", "v", "verbose"]):
				pass
			else:
				self.chrome_options.add_argument('--headless')
				self.chrome_options.add_argument('--disable-gpu')
		except:
			self.chrome_options.add_argument('--headless')
			self.chrome_options.add_argument('--disable-gpu')

		self.driver = webdriver.Chrome(str(chromedriver.ChromeDriverVersion.getPath()), options=self.chrome_options)
		self.scrape()
		self.driver.close()

		try:
			subprocess.call(["./getLength.out"])
		except:
			print("Was not able to call './getLenght.out' subprocess!")

	def replace(self):
		
		replacechars = ["1","2","3","4","5","6","7","8","9","0", "[",
						"]", "1.","2.","3.","4.","5.","6.","7.",
						"8.","9.","0.", "	", "     ", "  ", "(", ")", " A. ", " K. "]

		listtext  = self.text.split(" ")
		self.newlisttext = []

		for word in listtext:
			#word = word.strip()
			if(word[:-3].isupper() == True):
				word = ""

			for char in replacechars:
				word = word.replace(char, "")
			self.newlisttext.append(word)	

		return ' '.join(self.newlisttext)

	def scrape(self):
		for website in self.websites['websites']: 
			self.url = website['url']
			soup = BeautifulSoup(self.getPage(), 'html.parser')
			table = soup.find("table")
			main_menu_links = []
			for menu_link in table.find_all("option"):
				main_menu_links.append(os.path.join(website['url'],menu_link['value']))

			print("Found {} main menu links, now gathering all sub menu links!".format(len(main_menu_links))) 
			sub_menu_links = []
			for main_menu_link in tqdm(main_menu_links):
				try:
					self.url = main_menu_link
					soup = BeautifulSoup(self.getPage(), 'html.parser')
					table = soup.find("table")
					for sub_menu_link in table.find_all("a", href=True):
						sub_menu_links.append(os.path.join(website['url'], sub_menu_link['href']))
				except:
					pass

			print("Found {} sub menu links. now scraping them for latin text!".format(len(sub_menu_links)))

			f = open("latincorpus.txt", "w+")

			for text_website in tqdm(sub_menu_links):
				self.text = ""
				self.url = text_website
				try:
					soup = BeautifulSoup(self.getPage(), 'html.parser')
					body = soup.find("body")
					for p in body.find_all("p"):
						self.text += p.text

					f.write(self.replace())
				
				except Exception as e:

					#print(e)
					pass

			f.close()

	def getPage(self):

		try:
			page = self.driver.get(self.url)
			pageContent = self.driver.page_source
			return pageContent
		except:
			pass

	def checkIfFileExists(self):
		if(os.path.isfile("latincorpus.txt") == True):
			a = input("File allready exists! Overwrite? Y/N  \n --> ")
			if(a.upper() == 'Y'):
				os.remove("latincorpus.txt")
			else:
				print("No permission to overwrite {}! Shutting down!".format("latincorpus.txt"))
				exit()



if __name__ == "__main__":
	main()