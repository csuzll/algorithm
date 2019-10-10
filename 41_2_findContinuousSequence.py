def findContinuousSequence(s):
	if s < 3:
		return None
	else:
		result = []
		low,high = 1, 2
		mid = (1+s) // 2
		while low < mid:
			curSum = (low+high)*(high-low+1)//2
			if curSum == s:
				result.append(list(range(low, high+1)))
				high += 1
			elif curSum < s:
				high += 1
			else:
				low += 1
	return result

if __name__ == '__main__':
	test = 199
	print(findContinuousSequence(test))