class Node:
	def __init__(self,data,left=None,right=None):
		self.data = data
		self.right = right
		self.left = left


class bst:
	def create_node(self,data):
		return Node(data)
		
	def binary_insert(self,root,node):
		if root is None:
			return self.create_node(node)
		self.root = root
		self.node = node
		if root is None:
			root = node
		else:
			if root.data > node.data:
				if root.left is None:
					root.left = node
				else:
					self.binary_insert(root.left, node)

			else:
				if root.right is None:
					root.right = node
				else:
					self.binary_insert(root.right, node)
	
	def delete(self,data):
		if self.root:
			self.root == self.root.delete(data)
			
	def preorder(self,root):
		self.root = root
		if root:
			print(root.data)
			self.preorder(root.left)
			self.preorder(root.right)
			
	def postorder(self,root):
		self.root = root
		if root:
			self.preorder(root.left)
			self.preorder(root.right)
			print(root.data)

	def inorder(self,root):
		self.root = root
		if root:
			self.preorder(root.left)
			print(root.data)
			self.preorder(root.right)

root = None
bst = bst()
bst.binary_insert(root,10)
bst.binary_insert(root,7)
bst.postorder(root)

	"""
	def delete(self,data,find):
		self.data = data
		self.find = find
		if self.root:
			if root.data == find:
				root.data = None
				print("found"+self.find)
				
			self.preorder(root.left)
			self.preorder(root.right)
	""" 
