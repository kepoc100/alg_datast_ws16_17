
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

	def delete(self,node,data):
		if node is None:
			return None


		if data < self.node.data:
			node.left = self.delete(node.left, data)
		elif data > node.data:
			node.right = self.delete(node.right, data)
		else:
			if node.left is None and node.right is None:
				del node
			if self.node.left == None:
				temp = self.node.right
				del self.node
				return  temp
			elif self.node.right == None:
				temp = self.node.left
				del node
				return temp

			
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
r.binary_insert(r, bst(5))
r.binary_insert(r, bst(1))
r.binary_insert(r, bst(0))

print("preorder")
r.preorder(r)
#r.postorder(r)
#r.inorder(r)

r.delete(r,7)
print("preorder")
r.preorder(r)
