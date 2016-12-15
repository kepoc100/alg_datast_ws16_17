#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sortieren

Totale Ordnungen, transitiv, reflexiv, antisemetrisch


Listen sind totale Ordnungen
totale Ordnung alphabetisch Wörter

"""
# selection sort

# liste, dann kleinstes element an stelle 0, dann wieder kleinste an stelle 1 usw. in situ. complexity n square

def selection_sort(liste):
	counter = 0
	for x in range(len(liste)):
		if liste[x] < liste[counter]:
			print("liste[x]",liste[x],"<=",liste[counter])
			liste.insert(-1,liste[x])
			del liste[x]
			counter = counter+1
	return liste
		
print(selection_sort([3,2,1]))

# quick sort # divide and conquer -> problem in kleinere probleme aufteilen.

#def quick_sort(liste):
#	print(liste)
	
#quick_sort([1,2,3,6,7,4,8])
	
	
#merge sort 2 listen zusammenführen mit linearen zeitaufwand# zb reisverschlussprinzip mit drängeln ;)
"""
liste1 = [4,3,7,5,2,8]
liste2 = [3,7,6,1,2]

def merge_sort(liste1,liste2):
	# listen der länge 1
	def halbiere(liste):
		length = len(liste)
		print(length)
		
		
	halbiere(liste1)
	halbiere(liste2)
	
merge_sort(liste1,liste2)
"""
