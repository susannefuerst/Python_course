def average(args):
	return sum(args)/len(args)

def median(args):
	length = len(args)
	sortedList = sorted(args);
	if length % 2 == 1:
		return sortedList[int((length - 1)/2)]
	else: 
		return (sortedList[int(length/2)] + sortedList[int(length/2 - 1)])/2
	
if __name__ == "__main__":
	assert average([5,5,5,5,5]) == 5
	assert average([5,10,5,20]) == 10
	assert median([5,10,5,20]) == 7.5
	assert median([5,3,1,9,10]) == 5
	print('passed the test')	
