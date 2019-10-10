def findMinInorder(alist):
	length = len(alist)
	if length == 0:
		return False
	# 设置左右指针
	left,right = 0, length - 1
	mid = left # 特殊情况，排序数组本身
	while alist[left] >= alist[right]:
		if right-left == 1:
			mid = right
			break
		mid = (left + right) // 2
		# 特殊情况，左,右,中，相等（顺序遍历查找）
		if alist[left] == alist[mid] == alist[right]:
			return min(alist)
		# 中间大于等于左边，左指针移动到mid
		if alist[mid] >= alist[left]:
			left = mid
		# 中间小于等于右边，右指针移动到mid
		if alist[mid] <= alist[right]:
			right = mid
	return alist[mid]

alist = [1,2,3,4,5]
print(findMinInorder(alist))
print(findMinInorder([2, 2, 4, 5, 6, 2]))
print(findMinInorder([1,0,1,1]))