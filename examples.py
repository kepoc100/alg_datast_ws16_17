# last part of chapter introduction

# 1) write a function for finding the index fot the first occurence of an
# element in a list and compare experimentally the runtime with index()
# which one is more efficient?

# 2) write a funtcion which takes a list of integers as parameters and calculates
# the sum of all numbers in the list. compare the running time experimentally 
# with sum()- which one is more efficient?

import time

def sum_1(list):
	start_time=time.clock()
	sum = 0
	for item in list:
		sum = sum +item
	end_time=time.clock()
	a_time=end_time-start_time
	return sum, a_time
		
		

def find_first_occ(gesucht,list):
	start_time=time.clock()
	counter = -1
	for item in list:
		counter = counter +1
		if item == gesucht:
			end_time=time.clock()
			a_time=end_time-start_time
			return counter,a_time
		
def index(gesucht,list):
	start_time=time.clock()
	index = list.index(gesucht)
	end_time=time.clock()
	a_time=end_time-start_time
	return index ,a_time
	
liste1 = []
for x in range(100000000):
	liste1.append(0)
liste1.append(1)

start_time=time.clock()
sum = sum(liste1)
end_time=time.clock()
a_time=end_time-start_time
print "implemented SUM in C", sum, a_time
print "selbstprogrammiert SUM: ",sum_1(liste1)	
print "selbstprogrammiert FIND FIRST: ", find_first_occ(1,liste1)
print "implemented FIND FIRST in C ", index(1,liste1)