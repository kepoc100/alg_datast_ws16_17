import time
from random import randint

def create_200_lists():
	
	liste1 = []
	for x in range(0,200):
		liste2 = []
		for y in range(0,(x+1)*2):
			liste2.append(randint(0,100))
		liste1.append(liste2)
	return liste1

def measure_time(liste):
	
	for item in liste:
		start_time=time.clock()
		count_items = len(item)
		print (item[count_items//2])
		end_time=time.clock()
		a_time=end_time-start_time
		print('Access time:'+str(a_time))

if __name__=='__main__':
	
	liste = create_200_lists()
	measure_time(liste)
