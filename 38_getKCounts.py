# 获取k第一次出现的位置
def get_first_k(nums, k, first=0, last=None):
	if last==None:
		last = len(nums) - 1
	if first <= last:
		mid = (first + last) // 2
		if nums[mid] == k:
			if (mid > 0 and nums[mid-1]!=k) or mid == 0:
				return mid
			else:
				last = mid - 1
		elif nums[mid] > k:
			last = mid - 1
		else:
			first = mid + 1
		return get_first_k(nums, k, first, last)
	else:
		return -1

# 获取k最后一次出现的位置
def get_last_k(nums, k, first=0, last=None):
	if last==None:
		last = len(nums) - 1
	if first <= last:
		mid = (first + last) // 2
		if nums[mid] == k:
			if (mid < len(nums)-1 and nums[mid+1]!=k) or mid == len(nums)-1:
				return mid
			else:
				last = mid - 1
		elif nums[mid] > k:
			last = mid - 1
		else:
			first = mid + 1
		return get_last_k(nums, k, first, last)
	else:
		return -1

# 求次数
def get_k_counts(nums, k):
	length = len(nums)
	if length > 0:
		first = get_first_k(nums, k)
		last = get_last_k(nums, k)
		if first > -1 and last > - 1:
			return last-first+1
	return 0

if __name__ == '__main__':
	test = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
	print(get_k_counts(test, 4))