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
		
		
class Bst:
	def __init__()
