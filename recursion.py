x  = 1
# x is a reference to an object, which contains 1
# Scope: range of validity of identifiers. The resolution to an identifier x is done according to LEGB Rule
# Local, Enclosing, Global, Built-In

# Local
# inside a class/ function u have something local. so x is a current reference to an object in the current scope
# x is a class or function name defined by def or class in the current scope



# Enclosing
# Search is performed from the inside to the outside (indentation)
# most outside level is the module level
# an identifier that has the same name as an existing identifier from an enclosing scope overwrites this and makes it
# inaccessible!

# Global
# globale Variablen
# never a good idea
# 

# Built - In
# Example s = len("abc")

# Shadowing
# if we define len another time, the built-in identifier len is not available anymore
# this phenomenom is called Shadowing
# its gonna shadow the built in function


# Runtime Stack and Heap

# Runtime Stack                     |   Heap
#					                |
# [Activation Record] zeigt auf --> |   Objects
# adress, variables names       --> |   Objects


# Recursion


def sum_numbers_recursive(my_list):
	if len(my_list)==0:
		return 0
	return my_list[len(my_list)-1] + sum_numbers_recursive(my_list[:len(my_list)-1])

print sum_numbers_recursive([1,2,3,4,5,6])

# write a non recursive function which reverses a list

def non_recursive(my_list):
	recursive_list = []
	length = len(my_list)
	for x in my_list:
		recursive_list.append(my_list[length-1])
		length = length - 1	
	return recursive_list
		
print non_recursive([1,2,3,4,5,6,7])

def recursive_list(length,recur,my_list):
	length = len(my_list)
	recur.append(my_list[length-1])
	if not len(my_list) == len(recur):
		recursive_list(length,recur,my_list)
	else:
		return recur
	
	
print recursive_list(0,[],[1,2,3])
	
