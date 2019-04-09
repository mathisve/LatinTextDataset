#Mathis Van Eetvelde 2019
#refer to LICENSE.md for copyright and licensing info

import sys
import os

chromedriverMainPath = os.path.join(os.getcwd(), "chromedriver")

macpath = os.path.join(chromedriverMainPath, "macosdriver")
macchromedriverpath = os.path.join(macpath, "chromedriver")
zipmacpath = macchromedriverpath + "_mac64.zip"

windowspath = os.path.join(chromedriverMainPath, "windowsdriver")
windowschromedriverpath = os.path.join(windowspath, "chromedriver.exe")
zipwindowspath = windowschromedriverpath[:-4] + "_win32.zip" 

linuxpath = os.path.join(chromedriverMainPath, "linuxdriver")
linuxchromedriverpath = os.path.join(linuxpath, "chromedriver")
ziplinuxpath = linuxchromedriverpath + "_linux64.zip"

currentPath = ""
workingOS = sys.platform

def unzip(zippath, ospath):
	import zipfile
	print("Unzipping: " + zippath)
	currentZip = zipfile.ZipFile(zippath, 'r')
	currentZip.extractall(ospath)
	currentZip.close()
	if(workingOS == "linux" or workingOS =="darwin"):
		os.chmod(os.path.join(ospath, "chromedriver"), 754)

def getPath():
	try:
		global currentPath
		if(currentPath == ""):
			if(workingOS == "linux"):
				if(os.path.isfile(linuxchromedriverpath)):
					currentPath = linuxchromedriverpath
					print("Linux ChromeDriver found: " + currentPath)
				else:
					unzip(ziplinuxpath, linuxpath)
					getPath()

			elif(workingOS == "win32" or os == "cygwin"):
				if(os.path.isfile(macchromedriverpath)):
					currentPath = windowschromedriverpath
					print("Windows ChromeDriver found: " + currentPath)
				else:
					unzip(zipwindowspath, windowspath)
					getPath()

			elif(workingOS == "darwin"):
				if(os.path.isfile(macchromedriverpath)):
					currentPath = macchromedriverpath
					print("macOS ChromeDriver found: " + currentPath)
				else:
					unzip(zipmacpath, macpath)
					getPath()

			
			return currentPath
		else:
			return currentPath
	except Exception as e:
		print(e)
