def BinarySearch(alist, num):
	first = 0
	last = len(alist) - 1
	found = False
	while first <= last and not found:
		mid = (first + last) // 2
		if alist[mid] == num:
			found = True
		elif alist[mid] > num:
			last = mid - 1
		else:
			first = mid + 1
	return found

def BinarySearch2(alist, num, first=0, last=None):
	if last == None:
		last = len(alist)-1
	if first <= last:
		mid = (first+last) // 2
		if alist[mid] == num:
			return True
		elif alist[mid] > num:
			return BinarySearch2(alist, num, first, last = mid - 1)
		else:
			return BinarySearch2(alist, num, first=mid+1, last=last)
	else:
		return False

if __name__ == '__main__':
	arr = [1,2,3,4,5,6]
	print(BinarySearch(arr, 7))
	print(BinarySearch2(arr, 7))
			