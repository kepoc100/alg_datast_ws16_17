#[9,7,8,5,2,4]
# 0,1,2,3,4,5

class heap(object):
	
	def __init__(self):
		self.lst = []
		self.cnt = 0
	
	def build(self,list):
		self.lst = list(lst)
		self.cnt = len(lst)
		for i in range(len(lst)):
			self.sift_up(i)
	
	def __parent(self,index):
		
			
	def sift_up(self,index):
		if index == 0:
			return
		parent = Heap.__parent(index)
		while self.lst[parent] > self.lst[index] and parent >= 0:
			temp = self.lst[parent]
			self.lst[parent] = self.lst[index]
			self.lst[index] = temp
			index = parent
			parent = self.__parent(parent)
		
#sift down log n
		
		
		
h1 = heap()
h1.build([71,15,36,57,101])

