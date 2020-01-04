from selenium import webdriver
from selenium.webdriver.common.by import By
from ruamel.yaml import YAML
import os
import time
import hashlib

# YAML
yamlDrawings = YAML(pure=True)

# SELENIUM
driver = webdriver.Firefox()
driver.get("http://www.loto49.ro/arhiva-loto49.php")

elements = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[4]/td/div/span/table/tbody/tr")

#
# Create a new empty text file for the new Deawings
#	
drawingNewTextFile = open("NewDrawings.new","w")
drawingNewTextFile.close()

#
# Scanning the Table Elements from the page
# The Drawings in 6/49 Romanian Lottery
#
for element in elements:
	#
	# Mahe the Data Structure for the Drawing
	# as used for YAML
	#
	drawing = {}
	drawing['date'] = element.find_elements(By.TAG_NAME, "td")[0].text
	drawing['no1']  = element.find_elements(By.TAG_NAME, "td")[1].text
	drawing['no2']  = element.find_elements(By.TAG_NAME, "td")[2].text
	drawing['no3']  = element.find_elements(By.TAG_NAME, "td")[3].text
	drawing['no4']  = element.find_elements(By.TAG_NAME, "td")[4].text
	drawing['no5']  = element.find_elements(By.TAG_NAME, "td")[5].text
	drawing['no6']  = element.find_elements(By.TAG_NAME, "td")[6].text

	#
	# The Table has a Heading that must be omitted
	# 
	if (len(drawing['date'].split("-")) == 3):
		#
		# Creating the Drawing DateTime for handling the Drawing Directory in File System
		#	
		drawingYear = int(drawing['date'].split("-")[0])
		drawingMonth = int(drawing['date'].split("-")[1])
		drawingDay = int(drawing['date'].split("-")[2])
		
		drawingDate = time.localtime(time.mktime((drawingYear, drawingMonth, drawingDay, 0,0,0,0,0,0)))
				
		drawingDirectoryName = str(drawingDate.tm_year) +  "\\" + str(drawingDate.tm_mon).zfill(2) + "\\" + str(drawingDate.tm_mday).zfill(2) + "\\"
		drawingFileName = "1.yaml"
		drawingPathName = drawingDirectoryName + drawingFileName
		
		#
		# Creating the Directory for Drawing if it doesn't exist
		#
		if (os.path.isdir(str(drawingDate.tm_year)) == False):
			os.mkdir(str(drawingDate.tm_year))			
		if (os.path.isdir(str(drawingDate.tm_year) + "\\" + str(drawingDate.tm_mon).zfill(2) ) == False):
			os.mkdir(str(drawingDate.tm_year) +  "\\" + str(drawingDate.tm_mon).zfill(2))			
		if (os.path.isdir(str(drawingDate.tm_year) + "\\" + str(drawingDate.tm_mon).zfill(2) + "\\" + str(drawingDate.tm_mday).zfill(2)) == False):
			os.mkdir(str(drawingDate.tm_year) +  "\\" + str(drawingDate.tm_mon).zfill(2) + "\\" + str(drawingDate.tm_mday).zfill(2))
				
		#
		# Saving the Drawing in a temporary manner
		#		
		drawingFile = open(drawingPathName,"w")
		yamlDrawings.dump(drawing, drawingFile)
		drawingFile.close()
		
		#
		# Reading back the content if the Drawing
		# and Create the New Name of the File as SHA1
		#
		inputDrawingFile = drawingPathName
		openedDrawingFile = open(inputDrawingFile)
		readDrawingText = openedDrawingFile.read()
		openedDrawingFile.close()

		sha1Hash = hashlib.sha1(readDrawingText.encode())
		sha1Hashed = sha1Hash.hexdigest()
		
		drawingFileNameNew = sha1Hashed + ".yaml"
		drawingPathNameNew = drawingDirectoryName + drawingFileNameNew

		#
		# See if the SHA1 name exist
		# If exist delete the temporary file
		# If doesn't exist create de new file with SHA1 name
		#
		if (os.path.isfile(drawingPathNameNew) == True):
			os.remove(drawingPathName) 
			print("Old : ", drawingDirectoryName)
		else:
			os.rename(drawingPathName, drawingPathNameNew)
			print("New : ", drawingPathNameNew)
			drawingNewTextFile = open("NewDrawings.new","a")
			drawingNewTextFile.write(readDrawingText)
			drawingNewTextFile.close()
	
driver.quit()




