import os
from ruamel.yaml import YAML
from itertools import combinations	
import pprint

# YAML
yamlDrawings = YAML(pure=True)

# pprint
pp = pprint.PrettyPrinter(compact=True)

# Combinations
simples = combinations(range(1,50), 1) 
doubles = combinations(range(1,50), 2) 
triples = combinations(range(1,50), 3) 
quadrup = combinations(range(1,50), 4) 
quintup = combinations(range(1,50), 5) 
sixtupl = combinations(range(1,50), 6) 

# Lists

drawings = []

simplesList = {}
doublesList = {}
triplesList = {}
quadrupList = {}
quintupList = {}
sixtuplList = {}

for i in simples:
	simplesList[i] = 0
	
for i in doubles:
	doublesList[i] = 0

for i in triples:
	triplesList[i] = 0
	
for i in quadrup:
	quadrupList[i] = 0
	
for i in quintup:
	quintupList[i] = 0			
			
for i in sixtupl:
	sixtuplList[i] = 0
				
pp.pprint("Simples : {}".format(len(simplesList)))
pp.pprint("Doubles : {}".format(len(doublesList)))
pp.pprint("Triples : {}".format(len(triplesList)))
pp.pprint("Quadrup : {}".format(len(quadrupList)))
pp.pprint("Quintup : {}".format(len(quintupList)))
pp.pprint("Sixtupl : {}".format(len(sixtuplList)))

print("Current Directory : ", os.getcwd())

rootDir = os.getcwd()

for dirName, subdirList, fileList in os.walk(rootDir):
	if (not '.git' in dirName.split("\\")):
		for fname in fileList:
			if ('yaml' in fname.split(".")):
				openedDrawingFile = open(dirName + "\\" + fname)
				readDrawingText = openedDrawingFile.read()
				openedDrawingFile.close()
				
				drawingDictionary = yamlDrawings.load(readDrawingText)
				
				drawingList = []
				drawingListSorted = []
				
				#drawingList.append(drawingDictionary["date"])
				drawingList.append(int(drawingDictionary["no1"]))
				drawingList.append(int(drawingDictionary["no2"]))
				drawingList.append(int(drawingDictionary["no3"]))
				drawingList.append(int(drawingDictionary["no4"]))
				drawingList.append(int(drawingDictionary["no5"]))
				drawingList.append(int(drawingDictionary["no6"]))
				
				drawings.append(drawingList)				
				drawingListSorted = drawingList.sort()
				
				#
				# simples
				#			
				simplesDrawing = combinations(drawingList, 1)
				for i in simplesDrawing:
					simplesList[i] += 1

				#
				# doubles
				#
				doublesDrawing = combinations(drawingList, 2)				
				for i in doublesDrawing:
					doublesList[i] += 1
					
				#
				# triples
				#
				triplesDrawing = combinations(drawingList, 3)				
				for i in triplesDrawing:
					triplesList[i] += 1
					
				#
				# quadrup
				#
				quadrupDrawing = combinations(drawingList, 4)				
				for i in quadrupDrawing:
					quadrupList[i] += 1	
					
				#
				# quintup
				#
				quintupDrawing = combinations(drawingList, 5)				
				for i in quintupDrawing:
					quintupList[i] += 1	
					
				#
				# sixtupl
				#
				sixtuplDrawing = combinations(drawingList, 6)				
				for i in sixtuplDrawing:
					sixtuplList[i] += 1															
						
#pp.pprint(simples)

#for w in sorted(simplesList, key=simplesList.get, reverse=True):
#	print(w, simplesList[w])

#for w in sorted(doublesList, key=doublesList.get, reverse=True):
#	print(w, doublesList[w])

#for w in sorted(triplesList, key=triplesList.get, reverse=True):
#	print(w, triplesList[w])

#for w in sorted(quadrupList, key=quadrupList.get, reverse=True):
#	print(w, quadrupList[w])

for w in sorted(quintupList, key=quintupList.get, reverse=True):
	print(w, quintupList[w])
	
#for w in sorted(sixtuplList, key=sixtuplList.get, reverse=True):
#	print(w, sixtuplList[w])
