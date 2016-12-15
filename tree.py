
class bst:
	def __init__(self,data,left=None,right=None):
		self.data = data
		self.right = right
		self.left = left

		
	def binary_insert(self,root,node):
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
	
	def delete(self,data,find):
		self.root = root
		if root:
			print(root.data)
			self.preorder(root.left)
			self.preorder(root.right))
			
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

r = bst(3)
r.binary_insert(r, bst(7))
r.preorder(r)
print("")
r.postorder(r)
print("")
r.inorder(r)
r.delete(7)
r.inorder(r)
