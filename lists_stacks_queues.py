# abstract data type. no implementation details. sequence of data.

class PyList:
	def __init__(self, content=[], size=10):
		self._items = [None for x in range(size)]#oder [None]*size# size times non in our list
		self._size = size
		self._num_items = 0
		for elem in content:
			self._items.append2(elem)
	"""		
	def __getitem__(self,index):
		if index >= 0 and index < self._num_items:
			return self._items[index]
		raise IndexError("index out of range")
	
	def __setitem__(self, index, val):
		if index >= 0 and index < self._num_items:
			self._items[index] = val
			return 
		raise IndexError("index out of range")
	"""
	def __makeroom(self):
		newlen = (self._size // 4) + self._size + 1
		newlst = [None] + newlen
		for i in range(self.num_items):
			newlst[i] = self.items[i]
		self._items = newlst
		self._size = newlen
	
	def append2(self, item):
		if self._num_items == self._size:
			self.__makeroom()
		self._items[self._num_items] = item
		self._num_items += 1
		print self._items
		

		
	
lst = PyList([1,2,3])
lst.append(3)
