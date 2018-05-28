def absolute(number):
	if number >= 0:
		return number
	else:
		return -number

def maximum(args):
	numberOfArgs = len(args)
	if numberOfArgs == 2:
		if args[0] < args[1]:
			return args[1]
		else:
			return args[0]
	else:
		max = args[0]
		for i in range(0,numberOfArgs):
			max = maximum([max,args[i]])
		return max

if __name__ == "__main__":
	assert absolute(5) == 5
	assert absolute(-5) == 5
	assert maximum([1,2,3]) == 3
	assert maximum([4,3,2,1]) == 4
	print('passed the test')			

	
