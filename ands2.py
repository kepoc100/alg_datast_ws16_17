
def main():
	
	dictionary = {"John":"USA","Klaus":"Germany","Jean":"France"}
	neuer_key = raw_input("key: ")
	neuer_value = raw_input("value: ")
	dictionary[neuer_key] = neuer_value
	print dictionary 
if __name__ == '__main__':
	main()
