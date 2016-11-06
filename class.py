#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class.py
#  




class Greeting:
    def __init__(self, filename):
        self._greetings={}
        with open(filename, "r") as textfile:
			for line in textfile:
				splitting = line.split(" ")
				self._add_greeting(splitting[0], splitting[1])
		#	for line in textfile:
		#		sline=line.split(" ",1) #1 is max_splits
		#		if(len(sline)==2):
		#			[country,greeting]=sline
		#			self._add_greeting(country,greeting[0:-1])
    
    def _add_greeting(self,country,greeting):
        self._greetings[country]=greeting
        
    def greet(self,name,country):
        return self._greetings[country]+" "+name

    def __str__(self):
        print(self._greetings)

if __name__ == '__main__':
	Greeting1 = Greeting("greetings.txt")
	Greeting1.__str__()

        
