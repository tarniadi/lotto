import os
from ruamel.yaml import YAML
from itertools import combinations	
import pprint
from CommonCombinatorics import *

# YAML
yamlDrawings = YAML(pure=True)

# pprint
pp = pprint.PrettyPrinter(compact=True)

# Lists
drawings = []

simples    = TuplesDictionary(1)
doubles    = TuplesDictionary(2)
triples    = TuplesDictionary(3)
quadruples = TuplesDictionary(4)
quintuples = TuplesDictionary(5)
sextuples  = TuplesDictionary(6)

for dirName, subdirList, fileList in os.walk(os.getcwd()):
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
				simples.ProcessDrawing(drawingList)

				#
				# doubles
				#
				doubles.ProcessDrawing(drawingList)
					
				#
				# triples
				#
				triples.ProcessDrawing(drawingList)
					
				#
				# quadrup
				#
				quadruples.ProcessDrawing(drawingList)
					
				#
				# quintup
				#
				quintuples.ProcessDrawing(drawingList)
					
				#
				# sixtupl
				#													
				sextuples.ProcessDrawing(drawingList)
						
#pp.pprint(simples)

statisticsTextFile = open("Statistics.log","w")

statisticsTextFile.writelines("================================================================\n")

for w in sorted(simples.tuplesDictionary, key=simples.tuplesDictionary.get, reverse=True):
	statisticsTextFile.writelines(str(w) + " - " + str(simples.tuplesDictionary[w]) + "\n")

statisticsTextFile.writelines("================================================================\n")

for w in sorted(doubles.tuplesDictionary, key=doubles.tuplesDictionary.get, reverse=True):
	statisticsTextFile.writelines(str(w) + " - " + str(doubles.tuplesDictionary[w]) + "\n")

statisticsTextFile.writelines("================================================================\n")

for w in sorted(triples.tuplesDictionary, key=triples.tuplesDictionary.get, reverse=True):
	statisticsTextFile.writelines(str(w) + " - " + str(triples.tuplesDictionary[w]) + "\n")

statisticsTextFile.writelines("================================================================\n")

#for w in sorted(quadrupList, key=quadrupList.get, reverse=True):
#	print(w, quadrupList[w])

#for w in sorted(quintupList, key=quintupList.get, reverse=True):
#	print(w, quintupList[w])
	
#for w in sorted(sixtuplList, key=sixtuplList.get, reverse=True):
#	print(w, sixtuplList[w])

statisticsTextFile.close()
