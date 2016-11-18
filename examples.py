# last part of chapter introduction

# 1) write a function for finding the index fot the first occurence of an
# element in a list and compare experimentally the runtime with index()
# which one is more efficient?

# 2) write a funtcion which takes a list of integers as parameters and calculates
# the sum of all numbers in the list. compare the running time experimentally 
# with sum()- which one is more efficient?

import time
import multiprocessing
from threading import Thread

def sum_1(list):
	start_time=time.clock()
	sum = 0
	for item in list:
		sum = sum +item
	end_time=time.clock()
	a_time=end_time-start_time
	return sum, a_time
	
def sum(list):
	sum = 0
	for item in list:
		sum = sum +item
	return sum
	
def sum_multicore(list):
	cpucores = multiprocessing.cpu_count()
	n = len(list)/cpucores
	f = lambda list: [list[i:i+n] for i in range(0,len(list), n)]
	liste2 = f(list)
	for item in liste2:
		t = Thread(target=sum(liste2), args=(item,))
		t.start()
	
		

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
for x in range(100):
	liste1.append(0)
liste1.append(1)

start_time=time.clock()
sum = sum(liste1)
end_time=time.clock()
a_time=end_time-start_time
print "implemented SUM in C", sum, a_time
print "selbstprogrammiert SUM: ",sum_1(liste1)
print "Multi Core SUM: ",sum_multicore(liste1)	
#print "selbstprogrammiert FIND FIRST: ", find_first_occ(1,liste1)
#print "implemented FIND FIRST in C ", index(1,liste1)


# 1) write a non recursive function which takes two numbers x,n >= 0 as
# parameters and returns x hoch n

# 2) write a recursive function which takes two numbers x,n >= 0 as
# parameters and returns x hoch n

# compare the efficiency of those two functions
import math

def power_mal(x,y):
		if x and y >= 0:
			return x**y

def power(x,y):
	start_time=time.clock()
	p = 1
	for i in range(y):
		p = p * x
	end_time=time.clock()
	a_time=end_time-start_time
	return p, a_time
			
def recursive_power(x,y):
	if y == 0:
		return 1		
	return x * recursive_power(x,y-1)
'''	
# x to the power of y
print power(5000,5000)

start_time=time.clock()
rp = recursive_power(2,4)
end_time=time.clock()
a_time=end_time-start_time
print rp, a_time
'''

















