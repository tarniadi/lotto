from itertools import combinations

class TuplesDictionary(object):
	
	def __init__(self, elementsNumber):
		
		self.elementsNumber = elementsNumber
		self.tuplesDictionary = {}
		self.tuples = self.GetAllTuples(elementsNumber)
	
		for i in self.tuples:
			self.tuplesDictionary [i] = 0
			
	def ProcessDrawing(self, drawing):
		tuplesDrawing = combinations(drawing, self.elementsNumber)
		for i in tuplesDrawing:
			self.tuplesDictionary[i] += 1
			
	def GetAllTuples(self, elementsNumber):
		tuples = combinations(range(1,50), elementsNumber)
		tuplesDictionary = {}
		for i in tuples:
			tuplesDictionary[i] = 0
		return tuplesDictionary			
		
