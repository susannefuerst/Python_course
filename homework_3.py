def average(args):
	return sum(args)/len(args)

def median(args):
	length = len(args)
	sort(args)
	if length % 2 == 1: return (args[(length + 1)/2])
	else: return (args[(length/2)] + args[length/2 + 1])/2
