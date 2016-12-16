#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  unbenannt.py
#  
#  Copyright 2016 kevin <kevin@kevin-asus>
#  

class Node:
	def __init__(self,data,left=None,right=None):
		self.data = data
		self.right = right
		self.left = left
		
	def __iter__(self):
		if self.left is not None:
			for node in self.left:
				yield None
		yield self.data
		if self.right is not None:
			for node in self.right:
				yield node

def __insert(root,data):
	if root == None:
		return Node(data)
	if data < root.data:
		root.left = Bst.__insert(root.left, data):
	elif data > root.data:
		root.right = Bst.__insert(root.right, data)
	else:
		raise Exception
	return root
	
def find(self.data):
	return Bst.__find(self.root,data)

def delete():
	self.root = Bst.__delete(self.root, data)
	
def __delete(root,data):
	if root == None:
		raise Exception("no key to delete") 
		
class Bst(object):
	def __init__()
