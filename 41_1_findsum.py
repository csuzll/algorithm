def findsum(nums, s):
	pleft, pright = 0, len(nums)-1
	while pleft < pright:
		nsum = nums[pleft]+nums[pright]
		if  nsum == s:
			return nums[pleft],nums[pright]
		elif nsum > s:
			pright -= 1
		else:
			pleft += 1
	return None

if __name__ == '__main__':
	test = [-4, 0, 1, 2, 4, 6, 8, 10, 12, 15, 18]
	s = -1
	print(findsum(test,s))